class mingpian():
	def mp(self):
		while True:
			print("1、添加")
			print("2、查看")
			print("3、退出")
			u = inpu`t("请选择功能")
			if u == "1":
				list = []
				f = open("名片.txt","a")
				name = input("请输入名字")
				age = input("请输入年龄")
				career = input("请输入职业")
				list.append(name)
				list.append(age)
				list.append(career)
				f.write(str(list)+"\n")
				f.close()
				print("写入成功")
			elif u == "2":
				f = open("名片.txt","r")
				a = f.read()
				print(a)
				f.close()
			elif u == "3":
				break
b = mingpian()
b.mp()
