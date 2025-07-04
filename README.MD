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

## 🧠 Lead Score Logic

The tool checks for the presence of key terms in the company name such as:  
["AI", "Tech", "Analytics", "Machine Learning", "Data"]  
Each matched keyword contributes +2 points. This is a lightweight heuristic to help prioritize leads relevant to Caprae’s AI and SaaS investment theses.

## 📊 Sample Output Format

| Company     | Domain           | Email                   | Lead Score |
|-------------|------------------|--------------------------|------------|
| OpenAI      | openai.com       | info@openai.com          | 6          |
| Razorpay    | razorpay.com     | contact@razorpay.com     | 4          |
| Freshworks  | freshworks.com   | support@freshworks.com   | 6          |


## 🧾 License

This project is built solely for the Caprae Capital internship evaluation and is not intended for production use.

---

### 🙏 Built by Harsh Vardhan Chauhan

