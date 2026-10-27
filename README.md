# ☀️ AI-Powered Solar & Electrical Lead Qualifier

An enterprise-grade, automated lead qualification pipeline designed for solar and electrical installation businesses. Built using **n8n**, **Google Gemini AI**, **Google Sheets API**, and **Streamlit**.

---

## 🌟 Key Features

- ⚡ **Automated Webhook Ingestion:** Real-time data capture from custom web forms.
- 🧹 **Data Sanitization Node:** Custom JavaScript code node strips `+` signs, handles empty email/phone fallback parameters, and prevents false duplicate matches.
- 🛡️ **Smart Duplicate Prevention:** Pre-check mechanism against Google Sheets database using phone/email matching before triggering LLM calls.
- 🤖 **AI-Driven Lead Classification:** Google Gemini Chat Model analyzes project size and customer message to categorize leads (`HOT_LEAD`, `WARM_LEAD`, `LOW_PRIORITY`).
- 📧 **Instant Priority Routing:** Automatic Gmail dispatch for high-value commercial and residential leads.
- 📊 **Interactive Streamlit Dashboard:** Live user submission portal combined with real-time analytics and metric tracking.

---

## 🏗️ Architecture & Flow

1. **Webhook Ingestion:** Captures form payload.
2. **JavaScript Data Cleaner:** Formats phone strings and manages missing field fallbacks.
3. **Google Sheets Database Lookup:** Queries existing records for duplicate matching.
4. **Duplicate Decision Node:** Filters out existing entries to optimize AI credit usage.
5. **AI Agent Processing:** Evaluates request intent and assigns lead classification.
6. **Sheet Data Persistence:** Appends qualified entry into master leads tracker.
7. **Priority Filter & Email Dispatch:** Triggers instant email notification for `HOT_LEAD` status.

---

## 🛠️ Tech Stack

- **Automation Engine:** n8n (Docker Self-Hosted)
- **AI Model:** Google Gemini 1.5
- **Frontend / Dashboard:** Streamlit, Pandas
- **Backend Storage:** Google Sheets API
- **Notifications:** Gmail Node API
