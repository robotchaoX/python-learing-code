class Animal():
    def eat(self):
        print("eat--")

    def sleep(self):
        print("sleep--")

    def run(self):
        print("run--")

    def drink(self):
        print("drink--")


# class 子类名(父类名):  #子类继承父类的所有属性和方法
class Dog(Animal):
    # def eat(self):
    #     print("eat")
    #
    # def sleep(self):
    #     print("sleep")
    #
    # def run(self):
    #     print("run")
    #
    # def drink(self):
    #     print("drink")

    def bark(self):
        print("bark汪汪叫")


# 继承Animal类
class Cat(Animal):
    def catch(self):
        print("抓老鼠")


class XiaoTianQan(Dog):
    # # def eat(self):
    # #     print("eat")
    # #
    # # def sleep(self):
    # #     print("sleep")
    # #
    # # def run(self):
    # #     print("run")
    # #
    # # def drink(self):
    # #     print("drink")
    #
    # def bark(self):
    #     print("bark汪汪叫")
    def fly(self):
        print("fly")


# 创建一个哮天犬的对象
xtq = XiaoTianQan()
xtq.fly()  # 子类自定义的方法
xtq.bark()  # 子类继承父类的方法
xtq.eat()  # 子类继承父类的父类的方法
# xtq.catch()  # Dog类与Cat类是并列关系,不能混调方法
