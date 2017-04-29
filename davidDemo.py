import requests

#This gets a noddy json document and prints it out
#this apparently is a python 2.7 example

r = requests.get("http://jsonplaceholder.typicode.com/posts/1")
json = r.json()
print (r.status_code)
print (json)
