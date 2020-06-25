

# 父类
class Animal(object):
    def eat(self):
        print("Animal eat--")


# 子类
# class 子类名(父类名):  #子类继承父类的所有属性和方法
class Dog(Animal):

    def bark(self):
        print("Dog bark汪汪叫")


# 子类的子类
class XiaoTianQan(Dog):

    def fly(self):
        print("XiaoTianQan fly飞天")


# 创建一个哮天犬的对象
xtq = XiaoTianQan()

# 子类自定义的方法
xtq.fly()

# 子类继承父类的方法
xtq.bark()

# 子类继承父类的父类的方法
xtq.eat()
