

# 父类
# class Animal: # 经典类
# class Animal(): # 新式类,省略object
class Animal(object):  # 新式类,继承自object
    # 初始化
    def __init__(self):
        # 属性
        self.idStr = -1

    # # 方法
    # def eat(self):
    #     print("Animal eat--")

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

    # # 同名方法
    # # 重写父类方法  (定义一个跟父类同名的方法,覆盖父类的方法)
    # def eat(self):
    #     print("方法重写: Dog eat--")

    # 同名方法 调用同名属性
    # 重写父类方法
    def print_id(self):
        # 如果先调用父类的属性和方法,父类属性会覆盖子类属性,故需先调用自己的子类初始化
        self.__init__()  # ?? 不加这个自己的初始化,属性会是上一次调用init的属性
        print("方法重写: Dog print_id self.idStr:", self.idStr)

    # 子类调用父类的同名属性和方法:
    # 把父类的同名属性和方法再次封装(不好,推荐super()方法)
    def father_print_id(self):
        # 指明父类名 Animal. 调用父类方法
        Animal.__init__(self)  # 再次初始化
        Animal.print_id(self)

    def son_print_id(self):
        # 指明子类名 Dog. 调用子类方法
        Dog.__init__(self)  # 再次初始化
        Dog.print_id(self)


# 创建一个子类对象
wangcai = Dog()

# 子类重写父类方法
# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
# wangcai.eat()
wangcai.print_id()

# 子类重写父类属性
print(wangcai.idStr)


# 调用父类同名方法
wangcai.father_print_id()

# 调用子类同名方法
wangcai.son_print_id()
