import requests
from lxml import objectify

#import elementtree.ElementTree as ET

#This gets a noddy json document and prints it out
#metUrl = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/"

whsUrl = "http://services.english-heritage.org.uk/EnglishHeritageINSPIREDiscovery"
key = "78ded62a-0674-4e79-9e3e-c208cb69df19"
path = whsUrl + "?key=" + key
response = requests.get(path)
print(response.content)

xml_tree = objectify.fromstring(response.content)

for location in xml_tree.Location:
    print(location.attrib['id'])