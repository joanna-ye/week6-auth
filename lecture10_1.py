import requests
import secrets

base_url = "https://newsapi.org/v2/top-headlines"
params = {
"q": "new hampshire",
"apiKey": secrets.API_KEY
}

response = requests.get(base_url, params)
result = response.json()
articles = result["articles"]
for item in articles:
    print(item["title"], "-", item["source"]["name"])
