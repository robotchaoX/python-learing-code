

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

    def bark(self):
        print("Dog bark汪汪叫")


# 创建一个对象
wangcai = Dog()

# 父类方法
wangcai.eat()
wangcai.print_id()

# 父类属性
print(wangcai.idStr)

# 子类方法
wangcai.bark()
