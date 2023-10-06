import json
import requests
from uuid import uuid1
from bs4 import BeautifulSoup
from deep_translator import MyMemoryTranslator
from currency_converter import CurrencyConverter

#define the base url for the website scraping
base_url = 'http://books.toscrape.com/'

# Send a GET request to the main page
page = requests.get(base_url + 'index.html')

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(page.content, "html.parser")
articles = soup.find_all("article", class_="product_pod")

# Create a dictionary to store the books
books = dict()

for article in articles:
    # Generate a unique id for each book
    id = str(uuid1())
    title_container = article.find('h3')
    title = title_container.find('a').attrs['title']
    
    rating_container = article.find('p', class_="star-rating")
    # Get the class name of the rating
    rating = rating_container.attrs['class'][1]
    
    price_container = article.find('p', class_="price_color")
    # Remove the pound sign and the trailing white spaces
    price = price_container.text.replace('£','').strip()
    
    image_container = article.find('img', class_="thumbnail")
    image = base_url + image_container.attrs['src']
    
    # Get the text of the book from the deepai api
    r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': f"The text of {title} is: ",
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    
    # Due that the token is the quickstart one, it always return 401
    if r.status_code == 401:
        text = "Added dummy text due that the api token is a fake one"
    else:
        text = r.json()['output']
    # Translate the text to spanish and german using the MyMemoryTranslator
    text_es = MyMemoryTranslator(source='en-US', target='es-ES').translate(text)
    text_de = MyMemoryTranslator(source='en-US', target='de-DE').translate(text)
    
    price_eur = CurrencyConverter().convert(price, 'GBP', 'EUR')
    final_price_eur = round(float(price_eur), 2)
    
    books[id] = {
        'id': id,
        'title': title,
        'rating' : rating,
        'price' : price,
        'image' : image,
        'text' : text,
        'text_es': text_es,
        'text_de': text_de,
        'price_eur': final_price_eur
    }
with open('books.json', 'w') as outfile:
    json.dump(books, outfile)
    
