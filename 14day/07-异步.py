from multiprocessing import Pool
import time

def download():
	for i in range(10):
		#print("下载%d%%"%(i*10))
		time.sleep(1)
	return "下载完成"

def noti(arg):
	print(arg)
p = Pool()
#callback告诉线程,你下载完通过noti函数告诉我
#同步：看着它下载完
#异步：它下载　我去干别的　然后等它下载完成通知我
p.apply_async(download,callback=noti)
p.close()
for i in range(50):
	print("看电影中")
	time.sleep(1)
