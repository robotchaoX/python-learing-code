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
        # 传入父类对象调用父类方法,传入子类对象调用子类方法
        dog.game()  # 多态


# 创建狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianQuan("哮天犬")

# 创建小明对象
xiaoming = Person("小明")

# 小明调用狗玩耍
xiaoming.game_with_dog(wangcai)  # 传入父类对象调用父类方法,传入子类对象调用子类方法
