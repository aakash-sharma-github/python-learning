# Day 10
# News app using news api

import requests
import json

query = input("You are intrested in?? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-02-01&sortBy=publishedAt&apiKey=783e7233fc5d4b5995cef250a3284861"
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["author"])
    print(article["title"])
    print(article["description"])
    print("----------------------------------------------------------------")
