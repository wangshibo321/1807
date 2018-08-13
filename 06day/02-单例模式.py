class Dog():
	__instance = None
	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
dog1 = Dog()
print(id(dog1))

dog2 = Dog()
print(id(dog2))

dog3 = Dog()
print(id(dog3))



