class Women:
    def __init__(self, name):
        # 公有属性
        self.name = name
        # 私有属性
        # __两下划线开头__私有属性
        self.__age = 18

    # 公有方法
    def getAge(self):
        # 方法内部可以调用私有属性,修改私有属性
        print("私有属性 __age: %d" % self.__age)

    # 公有方法
    def setAge(self, age):
        # 方法内部可以调用私有属性,修改私有属性
        self.__age = age

    # 私有方法
    # __两下划线开头__私有方法
    def __secret(self):
        # 内部方法可以调用私有属性
        print("私有方法 %d" % self.__age)  # 私有属性

    # 公有接口调用私有方法
    def tellSecret(self):
        print("公有接口调用私有方法")
        # 对象内部的方法可直接访问私有属性和方法
        self.__secret()  # 私有方法


# 创建对象
xiaofang = Women("小芳")

# 公有属性
# 外部可直接调用对象公有属性和方法
print("公有属性name:", xiaofang.name)
# 私有属性
# 外部无法直接调用对象私有属性和方法
# print("私有属性 __age:", xiaofang.__age)  # error

# 公有方法
# 公有接口,修改私有属性
xiaofang.setAge(22)
# 公有接口,调用私有属性
xiaofang.getAge()

# 公有接口,调用私有方法
xiaofang.tellSecret()

# 私有方法
# 外部无法直接调用对象私有属性和方法
# xiaofang.__secret()
