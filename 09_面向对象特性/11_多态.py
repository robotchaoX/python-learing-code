"""
__title__ = ''
__author__ = 'chao'
__mtime__ = '18-12-7'
__version__=''
__packages__=','
__description__=''
"""


class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳的玩耍" % self.name)


class XiaoTianQuan(Dog):
    def game(self):  # 方法重写
        print("%s 飞到天上去玩耍" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))
        # 让狗玩耍
        dog.game()

# 创建狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianQuan("飞天旺财")
# 创建小明对象
xiaoming = Person("小明")
# 小明调用狗玩耍
xiaoming.game_with_dog(wangcai)




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
