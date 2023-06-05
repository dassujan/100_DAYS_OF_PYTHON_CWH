import requests


# response = requests.get("https://www.google.com")
# print(response.text)


# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": 'harry',
#     "body": 'bhai',
#     "userId": 12,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)
# print(response.text)


'''There is another module called BeautifulSoup which is used for web scraping in Python. I have personally used bs4 module to finish a lot of freelancing task.'''
from bs4 import BeautifulSoup # pip install bs4
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)