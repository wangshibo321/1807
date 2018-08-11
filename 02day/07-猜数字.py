class CSZ():
	def csz(self):
		import random
		a = random.randint(1,100)
		while True:
			b = int(input("请输入一个正整数"))
			if b > a:
				print("大啦")
			elif b < a:
				print("小啦")
			elif b == a:
				print("猜对啦")
				break
cai = CSZ()
cai.csz()
