import requests
url = "https://stephen-king-api.onrender.com/api/books"
res = requests.get(url)
print(res)

