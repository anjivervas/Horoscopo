import requests
from bs4 import BeautifulSoup

url='https://www.20minutos.es/horoscopo/'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="data_wide_table new_bar_table")
rows = table.find_all("tr")[1:]

item_prices = []

for row in rows:
    columns = row.find_all("td")
    item_name = columns[0].text.strip()
    price_text = columns[1].text.strip().replace("USD", "").replace(",", "").strip()
    
    try:
        price = float(price_text)
        item_prices.append((item_name, price))
    except ValueError:
        price = None 
    
    print(f"{item_name}: {price if price is not None else 'No disponible'}")