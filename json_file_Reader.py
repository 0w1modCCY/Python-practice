import urllib.request, urllib.parse, urllib.error
import json
import xml.etree.ElementTree as ET

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
sum = 0
print("Count:", len(info["comments"]))

for elem in info["comments"]:
    sum = sum + int(elem['count'])

print("Sum:",sum)
