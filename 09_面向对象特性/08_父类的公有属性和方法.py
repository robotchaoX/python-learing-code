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

    def __test(self):  # 私有方法访问自己的私有属性
        print("父类的 __私有方法: 公有属性%d  __私有属性%d" % (self.num1, self.__num2))

    def test(self):  # 公有方法访问自己的私有属性
        print("父类的公有方法: 公有属性%d 私有属性%d" % (self.num1, self.__num2))  # 公有方法调用自己的私有属性
        self.__test()  # 通过公有方法调用自己的私有方法/属性 来间接调用私有属性和方法



# B 继承 A
class B(A):
    def demo(self):

        # 访问父类的公有属性
        print("子类方法:父类公有属性 %d" % self.num1)


        # 调用父类的共有方法
        self.test()



b = B()
print(b)
print("公有属性:",b.num1)  # 公有属性
b.test()  # 外部调用父类的公有方法

b.demo()  # 外部调用子类的公有方法

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
