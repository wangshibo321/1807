class Lei():
	def __init__(self,name,color):
		self.name = name
		self.color = color


class Che(Lei):
	pass


class Sj(Lei):
	pass


che = Che("劳斯莱斯","宝石蓝")
print(che.name)
print(che.color)

sj = Sj("hhh","黑")
print(sj.name)
print(sj.color)

