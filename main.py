import requests
from bs4 import BeautifulSoup

base_url = 'http://books.toscrape.com/'
page = requests.get(base_url + 'index.html')

soup = BeautifulSoup(page.content, "html.parser")
articles = soup.find_all("article", class_="product_pod")
print(articles)
    
