# Gwendolyn Chu

'''
    UDP connection. C receives message from B.
'''

import socket
import sys

if len(sys.argv) != 2:
    print("Useage: python " + sys.argv[0] + " <listen port>")
    sys.exit(-1)

# s = socket for B
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind to receive message
s.bind(("0.0.0.0", int(sys.argv[1])))
print("Waiting..")

while True:
    # receives message from B
    data, addr = s.recvfrom(1024)
    data = data.decode("utf-8")
    print (data)

    if data == "bye":
        break
