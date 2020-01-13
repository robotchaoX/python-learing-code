class Animal:
    def eat(self):
        print("eat--")

    def sleep(self):
        print("sleep--")

    def run(self):
        print("run--")

    def drink(self):
        print("drink--")


# class 子类名(父类名):  #子类继承父类的所有属性和方法
class Dog(Animal):  # 继承
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


# 创建一个对象 - 狗对象
wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.bark()
