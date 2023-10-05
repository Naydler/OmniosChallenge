import requests
import time
from uuid import uuid1
from bs4 import BeautifulSoup

base_url = 'http://books.toscrape.com/'
page = requests.get(base_url + 'index.html')

soup = BeautifulSoup(page.content, "html.parser")
articles = soup.find_all("article", class_="product_pod")

books = dict()

start = time.time()

for article in articles:
    id = uuid1()
    title_container = article.find('h3')
    title = title_container.find('a').attrs['title']
    
    rating_container = article.find('p', class_="star-rating")
    rating = rating_container.attrs['class'][1]
    
    price_container = article.find('p', class_="price_color")
    price = price_container.text.replace('£','').strip()
    
    image_container = article.find('img', class_="thumbnail")
    image = base_url + image_container.attrs['src']
    
    r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': f"The text of {title} is: ",
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    
    if r.status_code == 401:
        text = "Error obtaining the text from the API, the api-key is not valid or the ratio has been exceeded"
    else:
        text = r.json()['output']
        
    books[id] = {
        'id': id,
        'title': title,
        'rating' : rating,
        'price' : price,
        'image' : image,
        'text' : text 
    }
    
    print(books[id])

    end = time.time()
    print(f"Time taken since start {end-start} seconds")
print(books)
    
    
