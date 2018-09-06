def a(b):
	def inner():
		print("滴滴滴~")
		b()
	return inner

@a
def c():
	print("嗒嗒嗒~")
c()
