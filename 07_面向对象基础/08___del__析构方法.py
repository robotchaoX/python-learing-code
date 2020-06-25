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


# 创建对象时，会自动调用初始化方法 __init__
# 有参构造
# tom是全局变量
tom = Cat("Tom猫")

print("---------------------")
# del 关键字可以删除一个对象,自动调__del__释放对象
del tom
print("---------------------")


# 创建对象时，会自动调用初始化方法 __init__
# 有参构造
lazy_cat = Cat("大懒猫")

print("********************")

# 运行结束自动调用__del__释放对象
