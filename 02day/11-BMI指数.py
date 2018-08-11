class BMI():
	def bmi(self):
		sg=float(input("请输入身高"))
		tz=float(input("请输入体重"))
		aa=tz/(sg*sg)
		if aa<18.5:
			print("过轻")
		elif aa>18.5 and aa<25:
			print("正常")
		elif aa>25 and aa<28:
			print("过重")
		elif aa>28 and aa<32:
			print("肥胖")
		elif aa>32:
			print("严重肥胖")
zhishu = BMI()
zhishu.bmi()
