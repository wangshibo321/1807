class STJDB():
	def stjdb(self):
		import random
		while True:
			a = random.randint(1,3)
			b = int(input("请输入1-石头 2-剪刀 3-布:"))
			if (b==1 and a==2)or(b==2 and a==3)or(b==3 and a==1):
				print("玩家赢")
			elif (a==1 and b==2)or(a==2 and b==3)or(a==3 and b==1):
				print("电脑赢")
			elif a==b:
				print("平局")
			else:
				print("你有病吧")
yx = STJDB()
yx.stjdb()

