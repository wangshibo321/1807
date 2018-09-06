
date = input("请输入年份")
N = int(date[0:4])
Y = int(date[4:6])
R = int(date[6:8])
a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
if (N%4==0)or(N%100!=0)or(N%400==0):
	c=1
else:
	d=2
day1=0
for i in range(1,Y+1):
	if i in a:
		day1+=31
	elif i in b:
		day1+=30
	elif c==1 and i==2:
		day1+=28
	elif i==2:
		day1+=29
if Y in a:
	day2=31
else:
	day2=30
day1 -= (day2-R)
print(day1)
	































'''
d = {"name":"laowang","age":12}
d2={}

for k,v in d.items():
	d2[v]=k
print(k)
print(d2)
'''
