import requests
from bs4 import BeautifulSoup
import csv

def fetch_product_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def parse_product_data(soup):
    products = []
    for item in soup.find_all('div', class_='s-main-slot s-result-list s-search-results sg-row'):
        for product in item.find_all('div', class_='s-result-item'):
            name = product.find('span', class_='a-text-normal')
            price = product.find('span', class_='a-price-whole')
            rating = product.find('span', class_='a-icon-alt')
            
            if name and price and rating:
                product_data = {
                    'name': name.get_text(strip=True),
                    'price': price.get_text(strip=True),
                    'rating': rating.get_text(strip=True),
                }
                products.append(product_data)
    return products

def save_to_csv(data, filename='products.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'price', 'rating'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    url = 'https://www.amazon.com/s?k=laptops'  # Example URL (search results for 'laptops')
    soup = fetch_product_data(url)
    products = parse_product_data(soup)
    save_to_csv(products)
    print(f"Scraped {len(products)} products and saved to 'products.csv'.")

if __name__ == "__main__":
    main()
