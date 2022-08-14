import socket

# Prepare socket and connect
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('data.pr4e.org', 80))

# Send command
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mySocket.send(cmd)

# Retrieve and print out data
while True:
    data = mySocket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
    
# Close socket
mySocket.close()