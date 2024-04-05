import requests
from bs4 import BeautifulSoup
import json
import datetime

url = "https://www.example.com"  # replace with the URL of the website you want to scrape
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

news = soup.find_all('div', class_='news')  # replace with the correct class name
category = soup.find_all('div', class_='category')  # replace with the correct class name

data = []

for i in range(len(news)):
    data.append({
        "id": i+1,
        "judul": news[i].text.strip().replace("\n", ""),
        "kategori": category[i].text.strip().replace("\n", ""),
        "tanggal": datetime.datetime.now().strftime("%d/%m/%Y - %H:%M"),
        "waktu_scraping": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

with open('BeritaTerbaru.json', 'w') as f:
    json.dump(data, f)