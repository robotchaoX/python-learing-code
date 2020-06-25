# 定义类
# class 类名():
#       类属性/类方法
#       def 类方法
#       self.类属性


# 定义类
class Cat():
    """这是一个猫类"""

    # 类方法
    # self指向当前对象,指的是当前调用该函数的对象
    def eat(self):
        print("小猫爱吃鱼")
        print("self地址:", self)  # 打印当前对象地址


# 创建猫对象
tom = Cat()
tom.eat()
print(tom)

# 再创建一个对象
lazy_cat = Cat()
lazy_cat.eat()
print(lazy_cat)

# 对象赋值,是同一个对象
copy_cat_2 = lazy_cat
copy_cat_2.eat()
print(copy_cat_2)
