import requests

#This gets a noddy json document and prints it out


#api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}

key = ""
lat = "50.727622"
lon = "-3.475646"
basePath = "http://api.openweathermap.org/data/2.5/weather?"
path = basePath + "&key=" + key + "?lat=" + lat + "&lon=" + lon

r = requests.get(path)
print (r.status_code)
json = r.json()



print (r.status_code)
print (json)



