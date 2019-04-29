# Gwendolyn Chu

'''
  Server and client exchange messages. Messages are saved and output when connection is closed.
'''

from socket import *
serverName = 'localhost'
serverPort = 12008
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
t = 0
l = []

while 1:
    if (t == 0):
        sentence1 = input('Please enter your message: ')
        l.append('message1: '+ sentence1)
        clientSocket.send(str.encode(sentence1))
        modifiedSentence = clientSocket.recv(1024)
        l.append('message2: '+ modifiedSentence.decode('utf-8'))
        print ('From Server: ', bytes.decode(modifiedSentence))
        t+=1

    elif (t == 1):
        sentence2 = input('Please enter your next message: ')
        l.append('message3: '+ sentence2)
        clientSocket.send(str.encode(sentence2))
        modifiedSentence = clientSocket.recv(1024)
        l.append('message4: '+ modifiedSentence.decode('utf-8'))
        print ('From Server: ', bytes.decode(modifiedSentence))
        break

clientSocket.close()
print(*l, sep = "\n")
