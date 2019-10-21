class Cat():
    """这是一个猫类"""
    def eat(self):
        print("%s 爱吃鱼" %self.name)  # self代表当前调用类的对象自己
    def drink(self):
        print("%s 爱喝水" %self.name)


tom = Cat()
tom.name = "tom猫"
tom.eat()
tom.drink()


print(tom)

# addr = id(tom)
# print("%d" % addr)
# print("%x" % addr)

# 再创建一个对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)



