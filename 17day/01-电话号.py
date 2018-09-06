import re
def checkphone(phone):
	ret = re.match(r"1[3456789]\d{9}$",phone)
	if ret:
		print("合法")
		return True
	else:
		return False
		print("不合法")
ret=checkphone("17698082316")
