from socket import *

a = socket(AF_INET,SOCK_DGRAM)

a.bind(("",6670))


while True:
	content = input("请输入内容：")
	a.sendto(content.encode("gb2312"),("192.168.43.222",6670))
	msg = a.recvfrom(1024)
	print("消息是：%s   来自IP：%s"%(msg[0].decode("gb2312"),msg[1][0]))

a.close()
