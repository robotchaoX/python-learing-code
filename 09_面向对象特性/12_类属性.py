class Tool(object):
    # 类属性,属于类
    count = 0  # 类属性,属于类??

    def __init__(self, name):
        self.name = name  # 实例属性

        # 调用类属性
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")
# 输出工具对象的总数
print(Tool.count)  # 类名.类属性名 # 调用类属性
