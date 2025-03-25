import streamlit as st
import requests

st.title('Simple Web Scraper')

# Input box to enter the URL
url = st.text_input('Enter URL to scrape:')

# Button to trigger scraping
if st.button('Scrape'):
    try:
        response = requests.post('http://backend:8001/scrape', json={'url': url})
        st.json(response.json())  # Display results from FastAPI
    except Exception as e:
        st.error(f"Error: {e}")
