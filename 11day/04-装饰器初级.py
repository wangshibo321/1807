def w1(fun):
	def inner():
		print("检查登录")
		fun()
	return inner


@w1#相当于pay = w1(pay)  语法糖
def pay():
	print("支付中")


pay()





















