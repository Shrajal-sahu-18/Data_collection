import requests
import pandas as pd
url = "https://stephen-king-api.onrender.com/api/books"
res = requests.get(url)
json_data = res.json()


df  = pd.json_normalize(json_data["data"])
print(df)



arl = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions.json"
res = requests.get(arl)
print(res.status_code)
json_data = res.json()
json_data