import time
import re
a = 0
b = 0
c = 0
c1 = 0
class RuZhu():
	def ruzhu(self):
		global a
		global c
		while True:
			self.name = input("请输入名字")
			self.ID = int(input("请输入手机号"))
			if len(ID) == 11:
				print("入住成功")
			else:
				print("重新输入")
			a.append(rz)
	def lidian(self):
		global b
		global c1
		while True:
			d = input("请输入姓名")
			print("离店")
			c1 = time.time()
			l+=1
			break

	def tongji(self):
		global a
		global b
		global c
		global c1

	def tuichu(self):
		print("退出系统")

	def dayin(self):
		while True:
			print("欢迎来到本宾馆")
			print("1、入住")
			print("2、离店")
			print("3、统计")
			print("4、退出")
			z = int(input("请输入序号"))
			if z==1:
				ruzhu()
			elif z==2:
				lidian()
			elif z==3:
				tongji()
			elif z==4:
				tuichu()
				break
Rz = RuZhu()
Rz.ruzhu()








	









