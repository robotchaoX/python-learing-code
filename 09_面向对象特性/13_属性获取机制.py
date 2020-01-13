class Tool(object):
    # 使用复制语句定义类属性
    count = 0

    def __init__(self, name):
        self.name = name  # 实例属性

        # 调用类属性
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")
# 输出工具对象的总数
print("向上查找类属性 %s" % tool3.count)  # 不推荐
print("类属性 %s" % Tool.count)  # 调用类属性
