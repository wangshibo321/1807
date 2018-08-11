class Phone():
    count = 0#类属性
    def __init__(self,color):
        self.color = color
        Phone.count+=1
    
    def call(self):
        print("打电话")




xiaomi = Phone("白色")
xiaomi1 = Phone("黑色")
xiaomi2 = Phone("灰色")

print(Phone.count)

