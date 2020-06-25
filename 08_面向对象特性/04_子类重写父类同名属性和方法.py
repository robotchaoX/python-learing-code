

# 父类
# class Animal: # 经典类
# class Animal(): # 新式类,省略object
class Animal(object):  # 新式类,继承自object
    # 初始化
    def __init__(self):
        # 属性
        self.idStr = -1

    # 方法
    def eat(self):
        print("Animal eat--")

    # 调用属性
    def print_id(self):
        print("Animal print_id self.idStr:", self.idStr)


# 子类
# 子类继承父类的所有属性和方法
# class 子类名(父类名):
class Dog(Animal):  # 继承

    # 初始化
    def __init__(self):
        # 同名属性
        self.idStr = 99

    # 同名方法
    # 重写父类方法  # 覆盖 # 方法重写(定义一个跟父类同名的方法,覆盖父类的方法)
    def eat(self):
        print("方法重写: Dog eat--")

    # 同名方法 调用同名属性
    # 重写父类方法
    def print_id(self):
        print("方法重写: Dog print_id self.idStr:", self.idStr)

    # # 子类方法
    # def bark(self):
    #     print("Dog bark汪汪叫")


# 创建一个子类对象
wangcai = Dog()

# 子类重写父类方法
# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
wangcai.eat()
wangcai.print_id()

# 子类重写父类属性
print(wangcai.idStr)

# 子类方法
# wangcai.bark()
