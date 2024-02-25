'''
Use the NewsAPI and the requests module to fetch the daily news related to
different topics. Go to: https://newsapi.org/ and explore the various options
to build you application


'''

import requests

api_key = "341aaa9179964da3880c368b48e16447"


def news():
    main_url= "https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key
    news= requests.get(main_url).json()
    #print(news)
    article= news["articles"]
##    print(article)

    news_article= []

    for arti in article:
        news_article.append(arti['title'])

    for i in range(5):
        print(i+1, news_article[i])

     


news()
