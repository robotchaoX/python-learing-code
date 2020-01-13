# class Cat():  # 没有继承,定义时类名后小括号可以省
class Cat:  # 没有继承,定义时类名后小括号可以省
    """这是一个猫类"""

    # 哪一个对象调用的方法，self就是哪一个对象的引用
    def eat(self):  # self 当前对象
        print("%s 爱吃鱼" % self.name)  # self代表当前调用类的对象自己

    def drink(self):
        print("%s 爱喝水" % self.name)


# 创建猫对象
tom = Cat()

# 对象名.属性名 临时添加属性 # 不推荐
tom.name = "tom猫"  # 添加属性 .name
tom.eat()
tom.drink()

print(tom)

# 再创建一个对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"  # 添加属性 .name
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)
