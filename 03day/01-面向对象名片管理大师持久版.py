class CarMan():
	def __init__(self):
		self.cards = []
	def insert(self):
		d = {}
		name = input("请输入名字")
		age = input("请输入年龄")
		d["name"] = name
		d["age"] = age
		self.cards.append(d)
		self.save()
	def find(self):
		print(self.cards)
	def change(self):
		pass
	def delete(self):
		pass
	def menu(self):
		self.open()#读取
		while True:
			num = int(input("请选择功能 1、添加 2、查看:"))
			if num == 1:
				self.insert()
			elif num ==2:
				self.find()
	def save(self):
		with open("data.data","w") as f:
			f.write(str(sele.cards))
	def open(self):
		f = open("data.data","r")
		self.cards = eval(f.read())
		#if len(f.read()) != 0:
			#self.cards = eval(f.read())
				#print(f.read())
cm = CardMan()
cm.menu()


