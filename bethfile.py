import requests

response = requests.post("https://airports.p.mashape.com/",
  json={"search":"bwi"},
  headers = {
    "X-Mashape-Key": "DERBPMreOxmshgHzMlXN4YRCAb9kp15wQKbjsngvAqBRQrFLiK",
    "Content-Type": "application/json",
    "Accept": "application/json"
  }
)

print ("output?")
print (response.headers)
print (response.status_code)
print (response.json())