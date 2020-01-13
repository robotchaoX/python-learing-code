class Women:
    def __init__(self, name):
        # 公有属性
        self.name = name
        # 私有属性
        self.__age = 18  # __两下划线开头__私有属性

    # 公有方法
    def showAge(self):
        print("我的年龄是 %d" % self.__age)  # 内部方法可以调用私有属性

    # 私有方法
    def __secret(self):  # __两下划线开头__私有方法
        # print("我的年龄是 %d" % self.age)
        print("我的年龄是 %d" % self.__age)  # 内部方法可以调用私有属性
        # 对象内部的方法可直接访问私有属性和方法


xiaofang = Women("小芳")

# 私有属性，在外界不能够被直接访问
# print("print .__age", xiaofang.__age)  # 外部不能直接调用对象私有属性和方法

# 私有方法，同样不允许在外界直接访问
# xiaofang.__secret()  # 外部不可直接调用私有方法

# python 伪私有属性 为 伪私有 , 实际就是偷偷改了名字 _类名+私有属性名
# 对象名._类名__私有属性 / 对象名._类名__私有方法 可以在外部调用私有属性或方法(不推荐)

# 伪私有属性，外部不能直接调用对象私有属性
print(xiaofang._Women__age)  # 私有 __age => _Women__age 实际名字
# 伪私有方法，外部不可直接调用私有方法
xiaofang._Women__secret()  # 私有 __secret() => _Women__secret() 实际名字
