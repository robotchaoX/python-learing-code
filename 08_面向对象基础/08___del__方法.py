class   Cat():
    def __init__(self,new_name):
        self.name = new_name
        print("%s 来了" % self.name)
    def __del__(self):
        print("%s 走了" % self.name)

# tom是全局变量
tom = Cat("Tom猫")
# del tom
print("-" * 20)



