import ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Send get request
html = urllib.request.urlopen('https://www.si.umich.edu', context=context).read()

# Make soup
soup = BeautifulSoup(html, 'html.parser')

# Get all href with anchor tag
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))