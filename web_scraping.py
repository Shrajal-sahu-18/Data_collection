import requests
url = "https://www.scrapethissite.com/pages/simple/"
res = requests.get(url)
with open("scraped_data/data1.html","w",encoding = "utf-8") as f:
    f.write(res.text)

from bs4 import BeautifulSoup
url = "https://www.scrapethissite.com/pages/simple/"
res = requests.get(url)
if (res.status_code) == 200:
    # print(res.content)
    print(res.headers)
    # print(res.text)
    
with open ("scraped_data/data1.html","w", encoding = "utf-8") as f:
    f.write(res.text)

from bs4 import BeautifulSoup
with open ("scraped_data/data1.html","r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content,"lxml")