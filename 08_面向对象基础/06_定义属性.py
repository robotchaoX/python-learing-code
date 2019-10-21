# class Cat():  # 定义时类名后小括号可以省??
class Cat:  # 定义时类名后小括号可以省??
    def __init__(self):  # 使用__init__初始化方法,定义属性
        print("自动调用初始化方法")
        self.name = "Tom"

    def eat(self):  # 定义方法
        print("%s 爱吃鱼" % self.name)


tom = Cat()
tom.eat()

