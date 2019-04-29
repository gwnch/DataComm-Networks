# Gwendolyn Chu

from socket import *
serverPort = 12008
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
t = 0
connectionSocket, addr = serverSocket.accept()

while 1:
    if (t == 0):
        sentence1 = connectionSocket.recv(1024)
        message1 = "Hello computer science student"
        connectionSocket.send(str.encode(message1))
        t+=1

    elif (t ==1):
        print ('second run')
        sentence2 = connectionSocket.recv(1024)
        message2 = "Bye"
        connectionSocket.send(str.encode(message2))
        break

connectionSocket.close()
