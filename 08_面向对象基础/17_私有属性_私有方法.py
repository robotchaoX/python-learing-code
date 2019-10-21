"""
__title__ = ''
__author__ = 'chao'
__mtime__ = '18-12-6'
__version__=''
__packages__=','
__description__=''
"""


class Women:
    def __init__(self, name):
        self.name = name
        # self.age = 18  # 共有属性
        self.__age = 18  # 私有属性  # __两下划线开头__私有属性

    # def secret(self):
    #     # print("我的年龄是 %d" % self.age)
    #     print("我的年龄是 %d" % self.__age)  # 内部方法可以调用私有属性
    def __secret(self):  # 私有方法  # __两下划线开头__私有方法
        # print("我的年龄是 %d" % self.age)
        print("我的年龄是 %d" % self.__age)  # 内部方法可以调用私有属性
        # 对象内部的方法可直接访问私有属性和方法


xiaofang = Women("小芳")
# print("print .age", xiaofang.age)  # 外部可直接调用对象共有属性和方法
# print("print .age", xiaofang.__age)  # 外部不能直接调用对象私有属性和方法

# xiaofang.__secret()  # 外部不可直接调用私有方法

# 对象名._类名__私有属性 / 对象名._类名__私有方法 可以在外部调用私有属性或方法(不推荐)
print("print .age", xiaofang._Women__age)  # 外部不能直接调用对象私有属性和方法
xiaofang._Women__secret()  # 外部不可直接调用私有方法

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
