import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = '42'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

url = serviceurl + urllib.parse.urlencode({'key': api_key,'address': address})
print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    info = json.loads(data)
except:
    info = None

print("Place id", info['results'][0]['place_id'])
