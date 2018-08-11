class Xs():
	list = []
	def a():
		while True:
			print("1、添加学生")
			print("2、删除学生")
			print("3、修改学生")
			print("4、查找学生")
			print("5、所有学生")
			print("6、退出系统")
			b()
	def b():
		Xz = int(input("请选择功能:"))
		if Xz == 1:
			add()
		elif Xz == 2:
			delete()
		elif Xz == 3:
			change()
		elif Xz == 4:
			find()
		elif Xz == 5:
			print_list()
		elif Xz == 6:
			exit()

	def add():
		stu = {}
		name = input("请输入学生名字")
		age = int(input("请输入学生年龄"))
		stu["name"] = name
		stu["age"] = age
		list.append(stu)
		print("添加成功")


xs = Xs()
print(xs)

                                                                      
