"""
__title__ = ''
__author__ = 'chao'
__mtime__ = '18-12-6'
__version__=''
__packages__=','
__description__=''
"""


class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法: 公有属性%d 私有属性%d" % (self.num1, self.__num2))

# B 继承 A
class B(A):
    def demo(self):
        # 子类不能直接访问父类的私有属性
        # print("直接访问父类的私有属性 %d" %self.__num2)

        # 子类不能直接调用父类的私有方法
        # self.__test()
        # super 也不能直接调用父类的私有方法
        # super(B, self).demo()
        pass


b = B()
print(b)

# 外界不允许访问对象的私有属性和私有方法
# print(b.__num2)  # 不能访问继承的私有属性
# b.__test()  # 不能访问继承的私有方法
b.demo()


"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃   神兽保佑   ┣┓
                ┃ 　永无BUG！  ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
