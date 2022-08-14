from cgitb import html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Send get request
html = urllib.request.urlopen('http://dr-chuck.com/page1.htm').read()

# Make soup
soup = BeautifulSoup(html, 'html.parser')

# Get all href with anchor tag
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))