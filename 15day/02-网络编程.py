from socket import *

a = socket(AF_INET,SOCK_DGRAM)

a.bind(("",6670))

a.sendto("哈哈哈".encode("gb2312"),("192.168.43.222",6670))

while True:
	msg = a.recvfrom(1024)
	print(msg[0].decode("gb2312"),msg[1][0])
	#print(msg)
a.close()
