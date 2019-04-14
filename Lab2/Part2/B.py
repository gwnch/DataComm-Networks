# Gwendolyn Chu

'''
    UDP connection with CRC. 40% chance that message is changed. Sends message to C. 
'''

import socket
import operator
import sys
import binascii
import struct
import random

def crc32(v):
   return binascii.crc32(v) & 0xffffffff

if len(sys.argv) != 4:
    print("Useage: python " + sys.argv[0] + " <listen port> <ip> <send port>")
    sys.exit(-1)

# s1 = socket for A
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind to receive message
s1.bind(("0.0.0.0", int(sys.argv[1])))
# s2 = socket for C
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Waiting...")

while True:
    # receives message from A via s1
    data, addr = s1.recvfrom(1024)
    # unpacks crc and data
    str,crc = struct.unpack("!50sL",data)
    str = str.decode("utf-8").replace("\0","")
    print("str:%s\ncrc:%X" % (str,crc & 0xffffffff))

    if str == "bye":
        ss = struct.pack("!50sL",str.encode('UTF-8'),crc)
        # sends message to C via s2
        s2.sendto(ss,(sys.argv[2],int(sys.argv[3])))
        break

    else:
        # 40% change that message is changed
        if random.randint(1, 100) < 40:
            str = str + 'A'
        ss = struct.pack("!50sL",str.encode('UTF-8'),crc)
        # sends message to C via s2
        s2.sendto(ss,(sys.argv[2],int(sys.argv[3])))
