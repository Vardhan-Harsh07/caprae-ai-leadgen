# 🚀 AI-Powered Lead Generation Tool (Caprae Internship Assignment)

This is a lightweight lead generation tool built for the **Caprae Capital Internship AI-Readiness Challenge**. It uses **SerpAPI** and smart scraping to enrich a list of company names with official domain names, potential emails, and a basic lead score.

---

## 🔍 Features

- Upload CSV of company names
- Automatically fetch official domain using Google Search (via SerpAPI)
- Extract potential emails from:
  - Google search snippets
  - `/contact` page scraping as fallback
- Simple lead scoring based on AI-relevant keywords
- Download results as a CSV
- Secure API key handling using `.env` file

---

## 🛠️ Tech Stack

- [Python 3.9+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [SerpAPI](https://serpapi.com/)
- `requests`, `re`, `pandas`, `dotenv`, `beautifulsoup4`

---

## 📦 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/leadgen-tool-caprae.git
   cd leadgen-tool-caprae
