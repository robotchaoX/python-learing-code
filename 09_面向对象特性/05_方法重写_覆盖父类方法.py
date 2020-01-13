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
    def bark(self):
        print("bark汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("fly")

    # 重写父类方法
    def bark(self):  # 覆盖 # 方法重写(定义一个跟父类同名的方法,覆盖父类的方法)
        print("方法重写: 叫得跟神一样")


xtq = XiaoTianQuan()
# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()
