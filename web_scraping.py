import requests
url = "https://www.scrapethissite.com/pages/simple/"
res = requests.get(url)
with open("scraped_data/data1.html","w",encoding = "utf-8") as f:
    f.write(res.text)

from bs4 import BeautifulSoup
url = "https://www.scrapethissite.com/pages/simple/"
res = requests.get(url)
