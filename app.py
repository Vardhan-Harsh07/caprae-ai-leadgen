import streamlit as st
import pandas as pd
import requests
import urllib.parse
import re
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup


load_dotenv()
SERPAPI_KEY = os.getenv('SERPAPI_KEY')


def scrape_email_from_contact_page(domain):
    try:
        url = f"https://{domain}/contact"
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            text = soup.get_text()
            emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
            return emails[0] if emails else ''
    except Exception as e:
        print(f"Scrape error: {e}")
    return ''

def get_domain_from_serpapi(company):
    query = urllib.parse.quote(company + " official site")
    url = f"https://serpapi.com/search.json?q={query}&api_key={SERPAPI_KEY}&engine=google"
    domain = ''
    email = ''
    try:
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            organic_results = data.get('organic_results', [])
            for result in organic_results:
                link = result.get('link', '')
                snippet = result.get('snippet', '')
                if not domain and link:
                    domain = urllib.parse.urlparse(link).netloc
                email_match = re.search(r"[\w\.-]+@[\w\.-]+", snippet)
                if email_match:
                    email = email_match.group(0)
                    break
            
            if domain and not email:
                email = scrape_email_from_contact_page(domain)
    except Exception as e:
        print(f"SerpAPI error: {e}")
    return domain, email


def simple_score(company):
    score = 0
    keywords = ['AI', 'Tech', 'Analytics', 'Machine Learning', 'Data']
    for word in keywords:
        if word.lower() in company.lower():
            score += 2
    return score


st.set_page_config(page_title="AI Lead Generator (SerpAPI)", layout="wide")
st.title("🚀 AI-Powered Lead Generator (SerpAPI Edition)")
st.markdown("Upload a CSV with company names to extract domains, emails, and lead scores.")

uploaded_file = st.file_uploader("Upload CSV with column 'Company'", type=['csv'])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if 'Company' not in df.columns:
        st.error("CSV must have a 'Company' column.")
    else:
        output_data = []
        with st.spinner('Fetching leads using SerpAPI and scraping contact pages...'):
            for _, row in df.iterrows():
                company = row['Company']
                domain, email = get_domain_from_serpapi(company)
                score = simple_score(company)
                output_data.append({
                    'Company': company,
                    'Domain': domain,
                    'Email (if found)': email,
                    'Lead Score': score
                })
        result_df = pd.DataFrame(output_data)
        st.success("Lead generation complete!")
        st.dataframe(result_df)

        csv = result_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Results", data=csv, file_name='leads.csv', mime='text/csv')


st.markdown("---")
st.markdown("Built by Harsh Vardhan Chauhan for Caprae Capital Internship Challenge")
