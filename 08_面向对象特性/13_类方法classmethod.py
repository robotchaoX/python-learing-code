# 类方法 @classmethod
# 用途:访问私有类属性,访问类属性


class Tool(object):
    # 类属性
    count = 0  # 类属性,属于类
    # 私有类属性
    __secret = "我是个废物"

    # 类方法
    @classmethod  # 类方法,属于类,没有self,cls类对象
    def show_tool_count(cls):  # cls类对象
        print("工具类对象的数量 %d" % cls.count)  # cls.类属性

    # 类方法
    @classmethod  # 类方法,属于类,没有self,cls类对象
    def show_tool_secret(cls):  # cls类对象
        print("工具类的秘密", cls.__secret)  # cls.类属性

    # 初始化
    def __init__(self, name):
        # 对象属性成员
        self.name = name

        # 调用类属性
        Tool.count += 1

        # cls 只能在@classmethod类内
        # cls.count += 1  # error
        # self 不能访问cls.类属性
        # self.count += 1  # self.count 创建对象属性


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")

# 调用类方法
Tool.show_tool_count()
Tool.show_tool_secret()

# 调用类属性
print("类属性 %s" % Tool.count)  # 类属性
# 私有类属性,类外无法访问
# print("类属性 %s" % Tool.__secret)
