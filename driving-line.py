
import socket
import struct
import os
import time





IP = '0.0.0.0'  # Receive any incoming UDP packet on this port
PORT = 1151  # Example port
ADDRESS = (IP, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ADDRESS)

FH5_DASH_BYTE_OFFEST = 12





while True:

    data, address = s.recvfrom(65536)
    print( "AI-Drive-line: " + str(int.from_bytes( data[309+FH5_DASH_BYTE_OFFEST:310+FH5_DASH_BYTE_OFFEST], "big")).ljust(10) +"Drive-line:"+  str(int.from_bytes( data[308+FH5_DASH_BYTE_OFFEST:309+FH5_DASH_BYTE_OFFEST], "big")).ljust(10) +  "AI-Br-line: " + str(int.from_bytes( data[310+FH5_DASH_BYTE_OFFEST:311+FH5_DASH_BYTE_OFFEST], "big")).ljust(10) +  "Br-line: " + str(int.from_bytes( data[304+FH5_DASH_BYTE_OFFEST:305+FH5_DASH_BYTE_OFFEST], "big")).ljust(10) )
  




   

