list = []
def mp():
	print("欢迎来到名片管理系统")
	while True:
		print("1、添加")
		print("2、查看")
		print("3、退出")
		a()
def a():
	b = int(input("请选用功能"))
	if b == 1:
		tj()
	elif b == 2:
		ck()
	elif b == 3:
		exit()		
def tj():
	stu = {}
	while True:
		name = input("请输入名字")
		stu["name"] = name
		age = int(input("请输入年龄"))
		stu["age"] = age
		list.append(stu)
		print("添加成功")
		break
def ck():
	print("姓名		年龄")
	for stu in list:
		print("%s		%d"%(stu["name"],stu["age"]))
mp()
