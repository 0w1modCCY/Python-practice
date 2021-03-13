import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter URL: ")
count = int(input("Enter count: "))
pos = int(input("Enter position: "))
primero = True

for i in range(count+1):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    if(primero):
        print("Retrieving: ", url)
        primero = False

    else:
        tags = soup('a')
        tag = tags[pos-1]
        print("Retrieving: ", tag.get('href', None))
        url = tag.get('href', None)
