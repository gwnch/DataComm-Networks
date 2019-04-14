# Gwendolyn Chu

'''
    UDP connection with CRC. Receives message from B. Checks if message has been changed.
'''

import socket
import operator
import sys
import binascii
import struct

def crc32(v):
    return binascii.crc32(v.encode())

if len(sys.argv) != 2:
    print("Useage: python " + sys.argv[0] + "<liseten port>")
    sys.exit(-1)

# s = socket for B
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind to receive message
s.bind(("0.0.0.0", int(sys.argv[1])))
print("Waiting...")

while True:
    # receives message from B via s
    data, addr = s.recvfrom(1024)
    # unpacks crc and data
    str,crc = struct.unpack("!50sL",data)
    str = str.decode("utf-8").replace("\0","")
    print(str)

    if str == "bye" or str == "byeA":
        break

    # compares CRCs to determine if message has been changed.
    if crc == crc32(str):
        print('original message')
    else:
        print('not original message')
