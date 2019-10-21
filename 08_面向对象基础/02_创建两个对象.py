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

# addr = id(tom)
# print("%d" % addr)
# print("%x" % addr)

# 再创建一个对象
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)



