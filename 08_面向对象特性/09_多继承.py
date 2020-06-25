

# 多继承的基类方法/属性有重名
class Sheep():
    # 初始化
    def __init__(self):
        # 类属性
        self.idStr = "I'm Sheep"

    # 类方法
    def print_id(self):
        print("Sheep print_id self.idStr:", self.idStr)


# 多继承的基类方法/属性有重名
class Tuo(object):
    # 初始化
    def __init__(self):
        # 类属性
        self.idStr = "I'm Tuo"

    # 类方法
    def print_id(self):
        print("Tuo print_id self.idStr:", self.idStr)


# 多继承
# 多继承可以让子类对象,同时具有多个父类的属性和方法
# 默认优先使用第一个继承类的属性和方法(如果有异议)
# 多继承的基类方法/属性有重名,继承顺序有影响
# class YangTuo(Tuo, Sheep):  # 优先使用Tuo
class YangTuo(Sheep, Tuo):  # 优先使用Sheep
    pass


# 创建子类对象
cnm = YangTuo()

# 父类方法
cnm.print_id()  # 默认优先使用第一个继承类的属性和方法

# 父类属性
print(cnm.idStr)  # 默认优先使用第一个继承类的属性和方法


# __mro__继承关系
# 确定多继承YangTuo类对象调用方法的顺序
print(YangTuo.__mro__)
