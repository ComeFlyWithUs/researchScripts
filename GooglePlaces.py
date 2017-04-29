import requests

#This gets a noddy json document and prints it out

#https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyBA1clTuoA4xzkQaqYdmLlM5VDVQeue8sE&location=50.727622,-3.475646&radius=500

basePath = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
key = "AIzaSyBA1clTuoA4xzkQaqYdmLlM5VDVQeue8sE"
location = "50.727622,-3.475646"
radius = "500"
path = basePath + "key=" + key + "&location=" + location + "&radius=" + radius

r = requests.get(path)
print (r.status_code)
json = r.json()



print (r.status_code)
print (json)



