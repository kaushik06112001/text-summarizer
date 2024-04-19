from text_summarize import text_summarizer
import requests
from bs4 import BeautifulSoup


# Define the News API endpoint and your API key
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "14fcdfa8144447cd9fe65ca72451d9cc"

#extraction of html content form website
def extract_content_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        body = soup.find_all("p",class_="ssrcss-1q0x1qg-Paragraph e1jhz7w10")#main showinf
        content=""
        for para in body:
            content += para.get_text().strip() + "\n"  # Concatenate paragraphs with a newline separator            
        return content        
    except Exception as e:
        print(f"Error occurred while extracting content: {e}")
        return None
    
# Function to fetch news articles and summarize them
def fetch_and_summarize_news(query, num_sentences=3):
    params = {
        "q": query,
        "apiKey": API_KEY,
        "pageSize": 4,
        "language": 'en',
        "domains": 'bbc.co.uk'  # Filter results by domain
    }
    response =  requests.get(NEWS_API_ENDPOINT, params=params)
    articles = response.json()["articles"]
    
    titles=[]
    urls=[]
    contents=[]
    summaries=[]
    for article in articles:
        text = extract_content_from_url(article["url"])
        if text:
            titles.append(article["title"])
            urls.append(article["url"])
            contents.append(text)  # Extract content from URL
            summary = text_summarizer(text, num_sentences)
            summaries.append(summary)
    return titles,urls,contents,summaries
