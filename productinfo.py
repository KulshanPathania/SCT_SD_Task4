import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_products(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve webpage")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    product_names = []
    product_prices = []
    product_ratings = []

    products = soup.find_all("div", class_="product")

    for product in products:
        name = product.find("h2")
        product_names.append(name.text.strip() if name else "N/A")

        price = product.find("span", class_="price")
        product_prices.append(price.text.strip() if price else "N/A")

        rating = product.find("span", class_="rating")
        product_ratings.append(rating.text.strip() if rating else "N/A")


    data = pd.DataFrame({
        "Name": product_names,
        "Price": product_prices,
        "Rating": product_ratings
    })


    data.to_csv("products.csv", index=False, encoding="utf-8")
    print("Data saved to products.csv")

url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
scrape_products(url)