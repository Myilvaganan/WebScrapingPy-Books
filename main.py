import requests
from bs4 import BeautifulSoup
import pandas as pd

SCRAPING_URL = "http://books.toscrape.com/catalogue/page-{PAGE_NO}.html"


def scrapingBooks(page):
    transform_url = SCRAPING_URL.replace('{PAGE_NO}', page)
    print(transform_url)
    html = requests.get(transform_url)
    soup = BeautifulSoup(html.text, 'lxml')
    article_div_wrapper = soup.find_all('article', attrs={'class': 'product_pod'})
    for parent in article_div_wrapper:
        book_image = parent.find('a', href=True)['href']
        book_title = parent.find('h3').find('a')['title']
        book_price = parent.find('p', class_='price_color').text[2:]
        book_availability = parent.find('p', class_='instock availability').text.strip()
        book_rating = parent.find('p')['class'][1]
        book = {
            'book_title': book_title,
            'book_image': book_image,
            'book_price': book_price,
            'book_availability': book_availability,
            'book_rating': book_rating
        }
        books.append(book)
    return


books = []
for page_no in range(1, 50):
    scrapingBooks(str(page_no))


store_data = pd.DataFrame(books)
store_data.index += 1
store_data.to_csv('books.csv')
