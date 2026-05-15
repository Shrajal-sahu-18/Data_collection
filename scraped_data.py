#creating mini project collecting data from scrap for ml model
import requests
from bs4 import BeautifulSoup 
import pandas as pd

page_count = 1
while True:
    url = f"https://quotes.toscrape.com/page/{page_count}/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"lxml")
    quotes = soup.select("div.quote")
    if not quotes:
        print("no valid page anymore....")
        break
    with open(f"scraped_data/quotes{page_count}.html","w",encoding ="utf-8") as f:
        f.write(res.text)
        print(f"downloading data from page{page_count}")
    page_count = page_count+1
    life_quotes = []
    for i in  range(1,11):
        with open(f"scraped_data/quotes{i}.html","r",encoding = "utf-8") as f:

   
    