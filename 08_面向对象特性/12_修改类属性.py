class Tool(object):
    # 类属性,属于类
    # 使用赋值语句定义类属性
    count = 0

    def __init__(self, name):
        # 实例属性
        self.name = name

        # 调用类属性
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 输出类属性

# 1 类名.类属性名
print("类属性", Tool.count)  # 类属性

# 2 对象名.类属性名 (不推荐)
print(tool1.count)  # 类属性,不推荐
# print(tool2.count)  # 类属性
# print(tool3.count)  # 类属性


# 修改类属性

# 1 类名.类属性名
Tool.count = 77  # 类属性
print("类属性", Tool.count)  # 类属性
print(tool1.count)  # 类属性,不推荐

# 2 对象名.类属性名 (不可以)
# ! 创建同名对象属性成员,覆盖类属性
tool3.count = 99  # error
print("tool3对象属性 %s" % tool3.count)  # 属性成员
print("类属性", Tool.count)  # 类属性
print("tool1对象类属性 %s" % tool1.count)  # 类属性
