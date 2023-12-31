# OmniosChallenge
<em> #OmniosChallenge </em>

Readme for the Book Scraping Program

This is a Python program designed to extract information from a website's books and then process and store this information in a JSON file. The program utilizes various Python libraries to perform these tasks, including BeautifulSoup, requests, deep_translator, and currency_converter.
Requirements

Make sure you have the following libraries installed in your Python environment before running the program:

    json: This library is used for JSON file manipulation.
    requests: It is used to make HTTP requests to the website from which information will be extracted.
    uuid: It is used to generate unique identifiers for each book.
    bs4 (Beautiful Soup): It is used to parse and extract data from the HTML content of the website.
    deep_translator: This library is used to translate the text of the books into different languages.
    currency_converter: It is used to convert the book prices from British pounds to euros.

You can install these libraries using the pip package manager as follows:

## Bash

pip install json requests uuid bs4 deep_translator currency_converter

## Usage


To use this program, follow these steps:

    Run the program in a Python environment with the aforementioned libraries installed.

    The program will send a GET request to the main page of the book website (http://books.toscrape.com/) and parse the HTML content to extract information about the books.

    For each book found on the page, the program will perform the following actions:
        Generate a unique identifier for the book.
        Extract the title, rating, price, and image of the book.
        Use the DeepAI API to generate text related to the book (due to the fictitious token limitation of the API, fictitious text is added if the request fails).
        Translate the text into Spanish and German using the deep_translator library.
        Convert the price from British pounds to euros.

    All the collected information will be stored in a dictionary and finally written to a JSON file named books.json in the current directory.

## Additional Notes


    Ensure you have an active internet connection for the program to make requests to the DeepAI API and the book website.

    The program uses a fictitious token for the DeepAI API, so requests cant return a 401 status code. Fictitious text is added in its place.

    Due to the translation API's limitations, the program can only translate a certain amount of characters per request (500). If there is a book text that is longer than this length it will explode. This could be mitigated capping the text to 500 length or changing the translation library.

    You can customize this program to suit your specific needs, such as changing the target website or translation API.

Enjoy using this program to scrape books and obtain information in multiple languages!
