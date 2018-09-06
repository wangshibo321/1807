from threading import Thread
import time

num = 0
flag = 1
def work1():
	global num,flag
	if flag == 1:
		for i in range(1000000):
			num += 1
		print("thread-1")
		print(num)
		flag = 2

def work2():
	global num
	while True:
		if flag == 2:
			for i in range(1000000):
				num += 1
	print("thread-2")
	print(num)
	

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)
