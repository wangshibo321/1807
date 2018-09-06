import re
ret = re.match(r"<(\w+)><(\w+)>.+</\2></\1>","<h1><li>老王</li></h1>")
print(ret)
