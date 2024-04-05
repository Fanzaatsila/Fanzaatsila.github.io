import requests
import json
from bs4 import BeautifulSoup
import datetime
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/run-python-script', methods=['GET'])
def run_python_script():
    subprocess.call("python ScrappingFile/main.py", shell=True)
    return "Python script run successfully"

URL = "https://www.tvonenews.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
latest = soup.find(class_="article-list-container")

title = latest.find_all("h2")
category = latest.find_all("h3")
date = latest.find_all(class_="ali-date content_center")

result = []
scraping_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
for i in range(len(title)):
    result.append({"id":i+1, "judul": title[i].text.strip().replace("\n", ""),
                   "kategori":category[i].text.strip().replace("\n", ""),
                   "tanggal":date[i].text.strip().replace("\n", ""),
                   "waktu_scraping": scraping_time
                   })
hasilJSON = json.dumps(result, indent=2)
JSONFile = open("ScrappingFile/BeritaTerbaru.json", "w")
JSONFile.write(hasilJSON)
JSONFile.close()

if __name__ == "__main__":
    app.run(debug=True)