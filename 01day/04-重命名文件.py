import os
a = input("请输入要重命名的文件夹")
files = os.listdir(a)
os.chdir(a)
print(os.getcwd())
for i in files:
	position = i.rfind(".")
	newname = i[:position]+"-腾讯"+i[position:]
	os.rename(i,newname)
