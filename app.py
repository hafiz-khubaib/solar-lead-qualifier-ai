import streamlit as st
import pandas as pd
import requests

# Page Layout Setup
st.set_page_config(page_title="Solar Lead Qualifier & Dashboard", page_icon="⚡", layout="wide")

st.title("⚡ Solar Lead Management & AI Qualifier System")
st.markdown("Automated lead intake, real-time Google Sheet tracking, and AI-powered duplicate filtering.")

# Navigation Tabs
tab1, tab2 = st.tabs(["📝 Submit New Lead", "📊 Live Metrics & Dashboard"])

# ==========================================
# TAB 1: USER LEAD SUBMISSION FORM
# ==========================================
with tab1:
    st.subheader("Customer Lead Submission Form")
    with st.form("lead_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            customer_name = st.text_input("Full Name *")
            phone = st.text_input("Phone Number (e.g. +9665XXXXXXXX) *")
            city = st.text_input("City / Location", value="Riyadh")
        with col2:
            email = st.text_input("Email Address (Optional)")
            property_type = st.selectbox("Property Type", ["Residential Villa", "Commercial Shop", "Apartment", "Commercial Factory"])
            system_size_kw = st.number_input("Estimated System Size (kW)", min_value=1, max_value=500, value=10)
        
        message = st.text_area("Project Details / Requirements")
        submit_btn = st.form_submit_button("🚀 Submit Lead Request")

    if submit_btn:
        if not customer_name or not phone:
            st.error("❌ Name aur Phone Number fill karna zaroori hai!")
        else:
            # Apne n8n Webhook ka URL paste karein
            WEBHOOK_URL = "YOUR_N8N_WEBHOOK_URL_HERE"
            
            payload = {
                "customer_name": customer_name,
                "phone": phone,
                "email": email,
                "city": city,
                "property_type": property_type,
                "system_size_kw": system_size_kw,
                "message": message
            }
            
            try:
                res = requests.post(WEBHOOK_URL, json=payload)
                if res.status_code == 200:
                    st.success("✅ Lead successfully submitted! n8n backend is processing the entry.")
                else:
                    st.error("⚠️ Backend server response error.")
            except Exception as e:
                st.error(f"❌ Server Connection Error: {e}")

# ==========================================
# TAB 2: LIVE METRICS & ANALYTICS DASHBOARD
# ==========================================
with tab2:
    st.subheader("📈 Live System Stats & Processed Leads")
    
    # Refresh Button
    if st.button("🔄 Refresh Data"):
        st.rerun()

    # Public Google Sheet CSV Link (Google Sheet ko File -> Share -> Publish to Web -> CSV karein)
    SHEET_CSV_URL = "YOUR_GOOGLE_SHEET_PUBLISHED_CSV_URL_HERE"

    try:
        # Load Data from Google Sheet
        df = pd.read_csv(SHEET_CSV_URL)

        # Top KPI Metrics Cards
        kpi1, kpi2, kpi3 = st.columns(3)
        
        total_leads = len(df)
        # Commercial / System Size >= 15 kW ko Hot Lead count kar sakte hain
        hot_leads = len(df[df['System Size'] >= 10]) if 'System Size' in df.columns else 0
        cities_count = df['City'].nunique() if 'City' in df.columns else 0

        kpi1.metric(label="Total Leads Captured", value=total_leads)
        kpi2.metric(label="High Priority / Hot Leads", value=hot_leads)
        kpi3.metric(label="Unique Cities Covered", value=cities_count)

        st.divider()

        # Data Table View
        st.subheader("📋 Registered Google Sheet Records")
        st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.info("💡 Connect your Google Sheet CSV URL to display live table and statistics metrics here.")
