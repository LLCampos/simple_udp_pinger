from socket import *

# Setups server
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"

while 1:
    ping, clientAdress = serverSocket.recvfrom(2048)

    if ping == "ping":
        serverSocket.sendto("pong", clientAdress)
