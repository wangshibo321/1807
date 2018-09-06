from socket import *

s = socket(AF_INET,SOCK_STREAM)#创建tcp
s.bind(("",6670))


s.listen(5)#监听

s1,info = s.accept()#等着接电话
print("有新链接了")

print(s1.recv(1024).decode("gb2312"))
s1.send("哈哈".encode("gb2312"))

s1.close()
s.close()
