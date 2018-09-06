class Dog(object):
	__instance = None
	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
	def __init__(self,name):
		self.name = name
dog1 = Dog("xiaoming")
dog2 = Dog("xiaoming")
