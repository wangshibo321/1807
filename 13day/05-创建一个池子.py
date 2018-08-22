from multiprocessing import Pool
import time

def show():
	for i in range(10):
		time.sleep(1)
		print("哈哈哈")

p = Pool(3) #创建一个池子，可以装无限个进程

for i in range(3):
	p.apply_async(show) #添加一个进程到池子里面　非阻塞添加进程　3个进程同时执行	
	#p.apply(show) #阻塞添加进程　30遍的任务　3个进程依次执行10遍
	print("添加成功")
p.close() #关闭池子
p.join() #不支持传超时时间
print("嘿嘿嘿")
