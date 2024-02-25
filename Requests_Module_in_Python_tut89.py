'''
Requests Module in Python

The Python Requests module is an HTTP library that enables developers to send HTTP Requests
in Python. This module enables you send HTTP requesnts using Python code and makes it
possible to interact with APIs and web servies.

Installation

pip install requests



Get Request

Once you have installed the Requests module, you can start using it to send HTTP requests.
Here is a simple example that sends a GET request to the Google homepage:


'''

import requests
from bs4 import BeautifulSoup

##print(dir(BeautifulSoup)) 

##response = requests.get("https://www.google.com")

##print(response.text)



'''
Post Request

Here is another example that sends a POST request to a web service and includes a custom header:

'''

##url = "https://api.example.com/login"
##headers = {
##    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
##    "Content-Type": "application/json"
##}
##data = {
##    "username": "myusername",
##    "password": "mypassword"
##}
##
##response = requests.post(url, headers=headers, json=data)
##
##print(response.text)

'''
In this example, we send a POST request to a web serviece t authenticate a user. We
include a custom User-Agent header and a JSON payload with the user's credentials ( سند )

bs4 MOdule :

There is another module called BeautifulSoup which is used for web scraping in Python.
I have personally used bs4 module to finish a lot of freelacing task.

'''
# Example:

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"

r= requests.get(url)

##print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)


url = "https://jsonplaceholder.typicode.com/posts"

data = {
     "title": 'Mohd Suhail',
     "body": 'MSP',
     "userId": 12,
   }
headers =  {
     'Content-type': 'application/json; charset=UTF-8',
   }
response = requests.post(url, headers=headers, json=data)

print(response.text)























































