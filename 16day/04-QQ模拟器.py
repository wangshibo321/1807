from socket import *

tcpClientSocket = socket(AF_INET,SOCK_STREAM)

serAddr = ("192.168.43.222",6670)
tcpClientSocket.connect(serAddr)

while True:
	sendData = input("send:")

	if len(sendData)>0:
		tcpClientSocket.send(sendData)
	else:
		break

	recvData = tcpClientSocket.recv(1024)
	print("recv:",recvData)
tcpClientSocket.close()

