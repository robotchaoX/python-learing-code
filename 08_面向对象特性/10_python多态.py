# 多态
# 传入不同的对象,产生不同的结果


# 父类
class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳的玩耍..." % self.name)


# 子类
class XiaoTianQuan(Dog):
    # 重写父类方法
    def game(self):  # 方法重写
        print("%s 飞到天上去玩耍..." % self.name)


# 人
class Person(object):
    def __init__(self, name):
        self.name = name

    #! 传入类对象形参
    # 根据传入的形参是父类对象还是子类对象,决定执行的方法
    # 传入不同的对象,执行不同的代码
    def game_with_dog(self, dog):  # dog类对象
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))
        # 传入父类对象调用父类方法,传入子类对象调用子类方法
        dog.game()  # 多态


# 创建小明对象
xiaoming = Person("小明")

# 创建狗对象
wangcai = Dog("旺财")
xtq = XiaoTianQuan("哮天犬")

# 小明调用狗玩耍
# 传入父类对象调用父类方法
xiaoming.game_with_dog(wangcai)  # 父类
# 传入子类对象调用子类方法
xiaoming.game_with_dog(xtq)  # 子类
