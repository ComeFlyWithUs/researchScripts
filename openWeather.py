import requests

lat = "50.727622"
lon = "-3.475646"
basePath = "http://api.openweathermap.org/data/2.5/weather?"
path = basePath + "lat=" + lat + "&lon=" + lon

response = requests.get(path)
print(response.status_code)
json = response.json()



print(response.status_code)
print(json)
