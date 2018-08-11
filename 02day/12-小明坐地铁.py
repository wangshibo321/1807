class XM():
	def xm(self):
		money = 0
		a = float(input("请输入距离:"))
		for i in range(1,31):
			for j in range(1,3):
				if a<=6:
					b=3
				elif a>6 and a<=12:
					b=4
				elif a>12 and a<=22:
					b=5
				elif a>22 and a<=32:
					b=6
				elif a>32:
					if (a-32)%20 == 0:
						b=6+(a-32)/20
					else:
						b=6+int((a-32)/20)+1
				if money>100 and money<=150:
					b=b*0.8
				elif money>150 and money<=400:
					b=b*0.5
				money=money+b


		print("一共花了%.02f元"%money)
ditie=XM()
ditie.xm()



