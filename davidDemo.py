import requests

#This gets a noddy json document and prints it out

r = requests.get("http://jsonplaceholder.typicode.com/posts/1")
print r.status_code
print r.headers
print r.content
