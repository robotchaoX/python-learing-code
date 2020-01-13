# class Cat():  # 没有继承,定义时类名后小括号可以省
class Cat:  # 没有继承,定义时类名后小括号可以省
    """这是一个猫类"""

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


# 创建猫对象
tom = Cat()
tom.drink()
tom.eat()
print(tom)

# 再创建一个对象
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

# 对象赋值,是同一个对象
lazy_cat2 = lazy_cat
print(lazy_cat2)
