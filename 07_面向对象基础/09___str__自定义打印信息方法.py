# 定义类
# class 类名():
#       类属性/类方法
#       def 类方法
#       self.类属性


# 定义类
class Cat():
    """这是一个猫类"""

    # __init__ 构造函数
    def __init__(self, new_name):  # 形参
        print("自动调用初始化方法")
        # 构造时添加属性成员
        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name
        print("%s 来了" % self.name)

    # __del__ 析构函数
    def __del__(self):
        print("%s 走了" % self.name)

    # __str__ 自定义print信息
    # print对象时,默认输出对象地址,__str__自定义打印信息
    def __str__(self):
        # 必须返回一个字符串
        return "print(对象)时 __str__ return: 我是小猫 %s" % self.name


tom = Cat("Tom猫")
print(tom)
