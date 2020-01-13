class A():
    def demo(self):  # 重名
        print("A 类--- demo 方法")


class B:
    def demo(self):  # 重名
        print("B 类 --- demo 方法")


# 多继承的基类方法有重名
# class C(A, B):  # A 类--- demo 方法
class C(B, A):  # B 类 --- demo 方法
    pass


# 创建子类对象
c = C()
# 多继承的基类方法有重名,所以具体哪个不一定??
c.demo()  # A / B 类不一定??

# 确定C类对象调用方法的顺序
print(C.__mro__)
