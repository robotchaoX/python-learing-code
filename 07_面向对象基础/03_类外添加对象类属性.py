# 定义类
# class 类名():
#       类属性/类方法
#       def 类方法
#       self.类属性


# 定义类
class Cat():
    """这是一个猫类"""

    # 类方法,调用类属性
    # self指向当前对象,指的是当前调用该函数的对象
    def printName(self):  # self 当前对象
        # 类内调用类属性
        # self.name 类属性
        print("我是: %s" % self.name)

    # 类方法,没有调用类属性
    def drink(self):
        print("小猫爱喝水")


# 创建猫对象
tom = Cat()

# 类外添加对象临时类属性 (不推荐)
# 对象名.属性名=值    # 类外临时添加类属性
tom.name = "tom猫"  # 类外添加类属性 .name

# 类外获取类属性
print(tom.name)

# 类内方法调用类属性
tom.printName()

# 类方法,没有调用类属性
tom.drink()
print(tom)

# 再创建一个对象
lazy_cat = Cat()
# 类外对象临时添加属性存在的问题
# 类方法内调用类属性,不临时添加属性无法调用
# lazy_cat.printName()  # error
# 类方法,没有调用类属性
lazy_cat.drink()
print(lazy_cat)
