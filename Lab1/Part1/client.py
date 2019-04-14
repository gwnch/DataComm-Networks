# Gwendolyn Chu

'''
    TCP connection made, sends a message, receives reply from
    server, and closes connection afer 2 replies.
'''

from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

i = 0
while i < 2:
    sentence = input('Talk to the server:')
    # send message to server
    clientSocket.send(str.encode(sentence))
    # receive message from server
    fromServer = clientSocket.recv(1024)
    print ('From Server:', bytes.decode(fromServer))
    i += 1

clientSocket.close()
