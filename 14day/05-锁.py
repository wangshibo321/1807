from threading import Thread,Lock
import time
num = 0
def work():
	global num
	m.acquire(True) #加锁　阻塞加锁
	for i in range(1000000):
		num += 1
	m,release() #释放锁
	print(num)
	print("thread-1")

def work2():
	global num
	m.acquire(True)
	for i in range(1000000):
		num += 1
	m.release()
	print(num)


