class Animal:
    def eat(self):
        print("eat--")

    def sleep(self):
        print("sleep--")

    def run(self):
        print("run--")

    def drink(self):
        print("drink--")


# 不用继承
class Dog:
    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")

    def run(self):
        print("run")

    def drink(self):
        print("drink")

    def bark(self):
        print("bark汪汪叫")


# 创建一个对象 - 狗对象
wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.bark()
