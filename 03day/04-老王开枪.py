class Ren():
	def __init__(self,name):
		self.name = name
		self.Qiang = None
	def zhuangzidan(self,dj,zd):#装子弹
		dj.addzidan(zd)#弹夹装子弹
	def zhuangdanjia(self,dj,Qiang):
		ak47.addDanJia(dj)
	def naqiang(self,qiang):
		self.qiang = qiang


class Qiang():
	def __init__(self,name):
		self.name = name
		self.dj = None




class DanJia():
	def __init__(self,RongLiang):
		self.RongLiang = RongLiang
		self.zds = []#子弹列表
	def addzd(self,zd)
		self.zds.append(zd)#装子弹





class ZiDan():
	def __init__(self,name,ShangHai):
		self.name = name
		self.shanghai = Shanghai
 




laowang = Ren("laowang")
ak47 = Qiang("ak47")
danjia = DanJia(40)
for i in range(40):
	zd = ZiDan("5.56",5)
	laowang.zhuangzd(dj,zd)
laowang.zhuangdanjia(dj,ak47)



