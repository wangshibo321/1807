class B():
	def handle(self):
		print("wo")
class A(B):
	def handle(self):
		B.handle(self)
		
C = A()
C.handle()
