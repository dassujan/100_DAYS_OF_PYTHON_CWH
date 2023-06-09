# Use the NewsAPI and the requests module to daily news related to different topics.
# Go to https://newsapi.org/ and explore the various options to build you application.
# API key: https://newsapi.org/v2/everything?q=tesla&from=2023-05-09&sortBy=publishedAt&apiKey=59b1388f368545b18b5639b065e9ab55


import requests
import json

query = input("What type of news are you interested in? ")  # Get the query from the user
url = "https://newsapi.org/v2/everything?q={query}&from=2023-05-09&sortBy=publishedAt&apiKey=59b1388f368545b18b5639b065e9ab55"
r = requests.get(url)   # Make an HTTP request
news = json.loads(r.text)   # Convert the response to a dictionary
# print(news, type(news)) # Print the dictionary
for article in news["articles"]: # Loop through the articles
    print(article["title"]) # Print the title of each article
    print(article["description"]) # Print the description of each article
    print("---------------------------------------------------------------") 