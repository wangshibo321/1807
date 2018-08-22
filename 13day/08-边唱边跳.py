from threading import Thread
import time

def sing():
	for i in range(10):
		print("singing!")
		time.sleep(1)

def dance():
	for i in range(10):
		print("dancing!")
t1 = Thread(target=sing)
t2 = Thread(target=dance)
t1.start()
t2.start()
#t1.join(3)
#t2.join(3)#等待子线程结束
print("哈哈哈哈哈哈哈")#主线程的代码
