def line_conf(a,b):
	def line(x):
		return a*x+b
	return line
#y = 2x+3
line = line_conf(2,3)
print(line(5))
print(line(6))
print(line(7))
def line1(a,b,x):
	return a*x+b
line1(2,3,5)
line1(2,3,6)
line1(2,3,7)
