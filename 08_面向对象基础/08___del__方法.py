# class Cat():  # 没有继承,定义时类名后小括号可以省
class Cat:  # 没有继承,定义时类名后小括号可以省
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


# tom是全局变量
tom = Cat("Tom猫")

# del 关键字可以删除一个对象
# del tom
print("-" * 20)
