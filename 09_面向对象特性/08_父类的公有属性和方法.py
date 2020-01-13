class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):  # 私有方法访问自己的私有属性
        print("父类的 __私有方法: 公有属性%d  __私有属性%d" % (self.num1, self.__num2))

    def test(self):  # 公有方法访问自己的私有属性
        print("父类的公有方法: 公有属性%d 私有属性%d" % (self.num1, self.__num2))  # 公有方法调用自己的私有属性
        self.__test()  # 通过公有方法调用自己的私有方法/属性 来间接调用私有属性和方法


# B 继承 A
class B(A):
    def demo(self):
        print("B : demo")
        # 1. 在子类的对象方法中，不能访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)

        # 2. 在子类的对象方法中，不能调用父类的私有方法
        # self.__test()

        # 3. 访问父类的公有属性
        print("子类方法:父类公有属性 %d" % self.num1)

        # 4. 调用父类的公有方法
        self.test()


# 创建一个子类对象
b = B()
print(b)

# 在外界访问父类的公有属性/调用公有方法
print("公有属性:", b.num1)  # 在外界访问父类的公有属性
b.test()  # 外部调用父类的公有方法
b.demo()  # 外部调用子类的公有方法

# 在外界不能直接访问对象的私有属性/调用私有方法
# print(b.__num2)
# b.__test()
