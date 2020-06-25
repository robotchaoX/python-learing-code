# 类属性,(类似c++static类属性)
# 类属性属于类,该类所有对象共有
# 类内直接使用的变量是类属性,self.使用的是实例属性


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
print(Tool.count)  # 类属性

# 2 对象名.类属性名 (不推荐)
print(tool1.count)  # 类属性,不推荐
print(tool2.count)  # 类属性
print(tool3.count)  # 类属性
