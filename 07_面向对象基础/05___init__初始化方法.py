# 定义类
# class 类名():
#       类属性/类方法
#       def 类方法
#       self.类属性


# 定义类
class Cat():
    """这是一个猫类"""

    # __init__ 初始化对象方法
    # 创建对象时,自动调用初始化方法__init__,专门用来定义一个类具有哪些属性的方法
    def __init__(self):
        print("创建对象时,自动调用__init__初始化方法")

        # 初始化时添加类属性成员
        # self.属性名 = 默认初始值
        self.name = "Tom猫"

    # self指向当前对象,指的是当前调用该函数的对象
    def printName(self):  # self 当前对象
        # 类内调用类属性
        # self.name 类属性
        print("我是: %s" % self.name)


# 创建对象时，会自动调用初始化方法 __init__
# 默认无参构造
tom = Cat()

# 类方法
tom.printName()

# 类属性
print(tom.name)
