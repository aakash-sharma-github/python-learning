# Day 89
# Response Module is used for getting or posting data from website or server.
import requests
# This module is used for beautifying the response.
from bs4 import BeautifulSoup
# response = requests.get("http://aakashsharma.com.np/?i=1")
# print(response.text) # you will get code of the link.

# url = "https://jsonplaceholder.typicode.com/posts"
# # posting request 
# data = {
#     "title": 'aakash',
#     "body": 'sudi',
#     "userId": 11,
# }
# headers = {
#     'Content-type': 'application/json; charset=utf-8',
# }

# response = requests.post(url, headers=headers, json=data)
# print(response.text)

# Beautify the code response.
url = "http://aakashsharma.com.np/?i=1"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

for heading in soup.find_all("body"):
    print(heading.text)
# print(soup.prettify())