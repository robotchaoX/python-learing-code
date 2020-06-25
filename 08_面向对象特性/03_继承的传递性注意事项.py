# 父类
class Animal(object):
    def eat(self):
        print("eat--")


# 子类1
class Dog(Animal):

    def bark(self):
        print("bark汪汪叫")


# 子类2
class Cat(Animal):
    def catch(self):
        print("抓老鼠")


# 子类的子类
class XiaoTianQan(Dog):

    def fly(self):
        print("fly")


# 创建一个哮天犬的对象
xtq = XiaoTianQan()
xtq.fly()  # 子类自定义的方法
xtq.bark()  # 子类继承父类的方法
xtq.eat()  # 子类继承父类的父类的方法

# Dog类与Cat类是并列关系,不能混调方法
xtq.catch()  # error
