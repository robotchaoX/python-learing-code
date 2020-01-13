class Game(object):
    # 类属性
    top_score = 99
    # 类私有属性
    __least_score = 1

    # 类方法
    @classmethod
    def show_top_score(cls):  # 类方法
        print("历史最高记录 %d" % cls.top_score)

    # 静态方法
    @staticmethod
    def show_help():  # 不需要任何参数
        print("帮助信息:让僵尸进入大门")

    def __init__(self, player_name):
        # 对象属性成员
        self.player_name = player_name  # 实例公有属性
        self.__lose_times = 1  # 实例私有属性

    # 成员函数
    def start_game(self):  # 实例公有方法
        print("%s 开始游戏啦..." % self.player_name)
        print("类公有属性 :top_score %d" % self.top_score)  # 实例调用类公有属性
        print("类私有属性:__least_score %d" % self.__least_score)  # 实例调用类私有属性
        print("类公有属性 :top_score %d" % Game.top_score)  # 类调用类公有属性
        print("类私有属性:__least_score %d" % Game.__least_score)  # 类调用类私有属性

    def __lose_game(self):  # 实例私有方法
        print("私有:失败次数")


# 创建类对象实例
game_p1 = Game("小明")  # 创建实例

# 调用类属性
print("类调用类属性", Game.top_score)  # 类调用类属性
print("实例调用类属性", game_p1.top_score)  # 实例调用类属性,不推荐

# 调用类方法
game_p1.show_top_score()  # 实例调用类方法
Game.show_top_score()  # 类调用类方法

# 调用静态方法
game_p1.show_help()  # 实例调用静态方法,不推荐
Game.show_help()  # 类调用类静态方法

# 调用实例公有方法
game_p1.start_game()  # 实例调用实例公有方法
# Game.start_game()  # 类不可以调用实例方法

# 访问实例公有属性
print("实例公有属性:", game_p1.player_name)  # 实例公有方法
# print("实例公有属性:", Game.player_name)  # 类不能调用普通属性


# 调用实例私有方法
# game_p1.__lose_game()  # 外部不可调用私有方法
# Game.__lose_game()  # 外部不可调用私有方法

# 访问实例私有属性
# print("实例私有属性:", game_p1.__lose_times)  # 外部不可调用私有属性
# print("实例私有属性:", Game.__lose_times)  # 外部不可调用私有属性
