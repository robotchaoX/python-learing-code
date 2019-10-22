"""
__title__ = ''
__author__ = 'chao'
__mtime__ = '18-12-6'
__version__=''
__packages__=','
__description__=''
"""


class Animal():
    def eat(self):
        print("eat--")

    def sleep(self):
        print("sleep--")

    def run(self):
        print("run--")

    def drink(self):
        print("drink--")


# class 子类名(父类名):  #子类继承父类的所有属性和方法
class Dog(Animal):
    def bark(self):
        print("bark汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("fly")

    # 当父类的方法不满足子类需求时,可对方法进行重写
    def bark(self):  # 覆盖 # 方法重写(定义一个跟父类同名的方法,覆盖父类的方法)
        print("方法重写: 叫得跟神一样")


xtq = XiaoTianQuan()
xtq.bark()

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
