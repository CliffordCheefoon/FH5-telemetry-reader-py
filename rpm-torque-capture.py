
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





x=list()
y=list()

open("data.csv", "w").close()
writefile = open("data.csv", "a")

writefile.write("RPM,Tq,Time\n")

while True:

    data, address = s.recvfrom(65536)
    print("Received: Current RPM:  "+  str(int(float('.'.join(str(ele) for ele in struct.unpack('f', data[16:20]))))).ljust(10) +"  Tq: " + str(int(float('.'.join(str(ele) for ele in struct.unpack('f', data[252+FH5_DASH_BYTE_OFFEST:256+FH5_DASH_BYTE_OFFEST]))))).ljust(10) +  "  Acc: " + str(int.from_bytes( data[303+FH5_DASH_BYTE_OFFEST:304+FH5_DASH_BYTE_OFFEST], "big")).ljust(10) +  "  Brake: " + str(int.from_bytes( data[304 +FH5_DASH_BYTE_OFFEST:305+FH5_DASH_BYTE_OFFEST], "big")).ljust(10) )
    writefile.write(str(int(float('.'.join(str(ele) for ele in struct.unpack('f', data[16:20]))))) +","+ str(int(float('.'.join(str(ele) for ele in struct.unpack('f', data[252+FH5_DASH_BYTE_OFFEST:256+FH5_DASH_BYTE_OFFEST]))))) +","+ str(time.time()) + "\n" ) 
 






   

