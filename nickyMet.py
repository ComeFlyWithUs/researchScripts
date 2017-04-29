import requests
from lxml import objectify

#import elementtree.ElementTree as ET

#This gets a noddy json document and prints it out
#metUrl = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/"

metUrl = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/datatype/sitelist"
key = "6913f2bc71fcb8d4796095c8a6037154"
path = metUrl + "?key=" + key
response = requests.get(path)
print(response.content)

xml_tree = objectify.fromstring(response.content)

for location in xml_tree.Location:
    print(location.attrib['id'])

#path = metUrl + "3840?res=3hourly&key=" + key
#print (response.status_code)

#tree = ET.parse("test.xml")
#doc = tree.getroot()
#thingy = doc.find('timeSeries')

#print thingy.attrib
#print(response.json())
