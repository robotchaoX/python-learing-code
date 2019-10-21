class Cat():
    """这是一个猫类"""
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫爱喝水")


tom = Cat()
tom.drink()
tom.eat()

print(tom)

addr = id(tom)
print("%d" % addr)
print("%x" % addr)
