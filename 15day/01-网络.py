from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.sendto("嘿嘿嘿".encode("gb2312"),("192.168.43.222",6670))

s.close()
