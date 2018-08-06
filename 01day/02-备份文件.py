name = input("请输入备份文件的名字(要有后缀名)")
f = open(name,"r")
content = f.read()
a = name.rfind(".")
f1 = open(name[:a]+"备份"+".txt","w")
f1.write(content)
f.close()
f1.close()

