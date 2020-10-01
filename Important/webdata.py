# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
from bs4 import *

url = input('Enter url - ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html)

count = int(input('Enter count'))
position = int(input('Enter position')) - 1

tags = soup('a')

url = tags[position].get('href', None)

n = 0

while n < count:
    n = n + 1
    print('Retrieving:', url)
    html =urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[position].get('href', None)
