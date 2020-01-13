class Person:
    # 有参构造
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        # 必须返回一个字符串
        return "print(对象)时 __str__ return: __str__ return: %s 体重 %s " % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5
        print("%s run 减肥后 %s" % (self.name, self.weight))

    def eat(self):
        self.weight += 1
        print("%s eat 吃饭后 %s" % (self.name, self.weight))


# 有参构造
xiao_ming = Person("小明", 75)
# 对象.方法 调用对象的方法
xiao_ming.run()
xiao_ming.eat()
print(xiao_ming)
