# Gwendolyn Chu

'''
    UDP connection. B receives message from A and sends to C.
'''

import socket
import sys

if len(sys.argv) != 4:
    print("Useage: python " + sys.argv[0] + "<listen port> <ip> <send port>")
    sys.exit(-1)

# s1 = socket for A
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind to receive message
s1.bind(("0.0.0.0", int(sys.argv[1])))
# s2 = socket for C
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # receives message from A via s1
    data, addr = s1.recvfrom(1024
    # sends message to C via s2
    s2.sendto(data,(sys.argv[2],int(sys.argv[3])))
    
    if data.decode("utf-8") == "bye":
        break
