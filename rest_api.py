import requests
url = "https://stephen-king-api.onrender.com/api/books"
res = requests.get(url)
json_data = res.json()
print(json_data)

