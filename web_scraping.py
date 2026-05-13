import requests
url = "https://www.scrapethissite.com/pages/simple/"
res = requests.get(url)
print(res)