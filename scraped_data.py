#creating mini project collecting data from scrap for ml model
import requests
from bs4 import BeautifulSoup 
import pandas as pd

page_count = 1
while True:
    url = f"https://quotes.toscrape.com/page/{page_count}/"
    res = requests.get(url)
    