# 定义类
# class 类名():
#       类属性/类方法
#       def 类方法
#       self.类属性


# 定义类
class Cat():
    """这是一个猫类"""

    # __init__ 有参初始化对象方法
    def __init__(self, new_name):  # 形参
        print("自动调用初始化方法")

        # 构造时添加属性成员
        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name

    # self指向当前对象,指的是当前调用该函数的对象
    def printName(self):  # self 当前对象
        # 类内调用类属性
        # self.name 类属性
        print("我是: %s" % self.name)


# 创建对象时，会自动调用初始化方法 __init__
# 有参构造
tom = Cat("Tom猫")

# 类方法
tom.printName()

# 类属性
print(tom.name)
