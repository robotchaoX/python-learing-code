class Tool(object):
    # 类属性
    count = 0  # 类属性,属于类??

    # 类方法
    @classmethod  # 类方法,属于类,没有self,是cls??
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)  # cls.类属性

    def __init__(self, name):
        # 对象属性成员
        self.name = name
        # 调用类属性
        Tool.count += 1
        # cls.count += 1  # cls 只能在@classmethod类内
        # self.count += 1  # self 不能访问cls.类属性 # self.count 创建对象属性


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")

# 调用类方法
Tool.show_tool_count()
# 调用类属性
print("类属性 %s" % Tool.count)  # 类属性
