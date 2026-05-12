import requests
import pandas as pd
url = "https://stephen-king-api.onrender.com/api/books"
res = requests.get(url)
json_data = res.json()


df  = pd.json_normalize(json_data["data"])
print(df)
