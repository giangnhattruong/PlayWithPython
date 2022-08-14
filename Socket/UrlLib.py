import urllib.request, urllib.parse, urllib.error

# Send get request
bodyData = urllib.request.urlopen('http://dr-chuck.com/page1.htm')

# Print response body
for line in bodyData:
    line = line.decode().strip()
    print(line)