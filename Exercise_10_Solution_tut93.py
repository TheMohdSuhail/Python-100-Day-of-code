'''
#Exercise 10 Use the NewsAPI and the requests module to fetch the daily news related to
different topics. Go to: https://newsapi.org/ and explore the various options to build you
application


'''

import requests

import json

api_key = "341aaa9179964da3880c368b48e16447"


query = input("What type of news are you interested in? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2023-07-01&sortBy=publishedAt&apiKey={api_key}"

r = requests.get(url)

news = json.loads(r.text)

##print(news,type(news))



for article in news["articles"]:
   print(article["title"])
   print(article["description"])
   print("\n_____________________________________________________________________________\n")

    
