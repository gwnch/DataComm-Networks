# Gwendolyn Chu

'''
    UDP connection. A sends message to B.
'''

import socket
import sys

if len(sys.argv) != 3:
    print("Useage: python " + sys.argv[0] + " <ip> <listen port>")
    sys.exit(-1)

# s = socket for B
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    print("Input text:")
    text = sys.stdin.readline().strip()
    # sends message to B
    s.sendto(text.encode(),(sys.argv[1],int(sys.argv[2])))
    
    if text == "bye":
        break
