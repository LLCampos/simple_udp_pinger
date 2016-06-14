from socket import *
import time

# Sends 10 ping messages and calculates Round Trip Times (RTTs).

serverName = '10.101.228.223'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Raises exception if an operation takes longer than one second.
clientSocket.settimeout(1)

soma = 0
for i in range(10):

    # Sends a "ping" and waits for the server to return a "pong".

    clientSocket.sendto("ping", (serverName, serverPort))
    send_time = time.clock()

    try:
        pong, serverAdress = clientSocket.recvfrom(2048)
        receive_time = time.clock()

        if pong == "pong":

            rtt = receive_time - send_time
            soma += rtt

            print "RTT for ping %s: %s seconds." % ((i + 1), rtt)
    except timeout:
        print "Socket %s was lost" % (i + 1)


print
print "Average RTT: %s seconds." % (soma / 10)

clientSocket.close()
