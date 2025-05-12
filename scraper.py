
import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_ai_litigation():
    url = 'https://www.example.com/ai-litigation-news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    cases = []
    for article in soup.select('.article'):
        title = article.select_one('.title').text
        company = article.select_one('.company').text if article.select_one('.company') else 'Unknown'
        location = article.select_one('.location').text if article.select_one('.location') else 'Unknown'
        date = article.select_one('.date').text if article.select_one('.date') else 'Unknown'
        topic = article.select_one('.topic').text if article.select_one('.topic') else 'AI'
        link = article.select_one('a')['href']
        summary = article.select_one('.summary').text if article.select_one('.summary') else 'No summary.'
        
        cases.append({
            'Case Title': title,
            'Company Involved': company,
            'Court/Location': location,
            'Date': date,
            'AI Topic': topic,
            'Link': link,
            'Summary': summary
        })
    
    df = pd.DataFrame(cases)
    df.to_csv('litigation_index.csv', index=False)
    print("Scraped and saved.")

if __name__ == "__main__":
    scrape_ai_litigation()
