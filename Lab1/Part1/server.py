# Gwendolyn Chu

'''
    TCP connection made, receives message from client, server replies to
    message, sends "bye", and closes connection.
'''

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
connectionSocket, addr = serverSocket.accept()
i = 0

while i < 2:
    # receive message from client
    fromClient = connectionSocket.recv(1024)

    if i == 0:
        # first reply
        connectionSocket.send(str.encode('cool'))

    else:
        # second reply
        connectionSocket.send(str.encode('bye!'))

    i += 1

connectionSocket.close()
