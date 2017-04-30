import requests

lat = "50.727622"
lon = "-3.475646"
basePath = "http://api.openweathermap.org/data/2.5/weather?"

key = "6913f2bc71fcb8d4796095c8a6037154"

weatherObj = {}

path = basePath + "lat=" + lat + "&lon=" + lon + "&APPID=" + key

response = requests.get(path)
print(response.status_code)
json = response.json()

print(response.status_code)
print(json)
print(json["weather"])
print(json["main"])
weatherObj["weather"] = json["weather"][0]["main"]
weatherObj["temperature"] = json["main"]["temp"]

print(str(weatherObj))