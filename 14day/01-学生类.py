class Student():
	count = 0
	def __init__(self,name):
		self.name = name
		Student.count += 1
a = Student("A")
b = Student("B")
c = Student("C")
print(Student.count)
