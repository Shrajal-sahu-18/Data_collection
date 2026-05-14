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
all_h3 = soup.find_all("h3")
all_countries = []
for h3 in all_h3:
    name = (h3.get_text(strip = True))
    population = (h3.find_next("div").select("span.country-population")[0].get_text(strip = True))
    all_countries.append([name,population])
    print(h3.attrs())
all_countries
import pandas as pd
df = pd.DataFrame(all_countries,columns = ["Name","Population"])
df.to_csv("scraped_data/Data.csv",index = False)