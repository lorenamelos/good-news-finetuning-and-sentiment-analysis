import streamlit as st
import gradio as gr
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import dotenv
from dotenv import load_dotenv, find_dotenv
import os

# LOADING THE API KEY:

# Load environment variables from .env file
# load_dotenv(find_dotenv())

# api_key = os.environ.get("NEWS_API_KEY")



import streamlit as st
import requests
from datetime import datetime
import os

def fetch_news(api_key, query='positive OR good OR uplifting', language='en'):
    url = f"https://newsapi.org/v2/everything?q={query}&language={language}&from={datetime.today().date()}&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return articles

positive_keywords = ['good', 'positive', 'uplifting', 'happy', 'joyful']

def is_positive(article):
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    return any(keyword in title or keyword in description for keyword in positive_keywords)

def filter_positive_news(articles):
    return [article for article in articles if is_positive(article)]

def main():
    st.title("Good News Today")

    api_key = os.getenv("NEWS_API_KEY")

    if api_key:
        articles = fetch_news(api_key)
        positive_articles = filter_positive_news(articles)

        if positive_articles:
            for article in positive_articles:
                st.subheader(article['title'])
                st.write(article['description'])
                st.write(f"[Read more]({article['url']})")
                st.write("---")
        else:
            st.write("No positive news found today.")
    else:
        st.error("API key not found. Please set the NEWS_API_KEY environment variable.")

if __name__ == "__main__":
    main()
