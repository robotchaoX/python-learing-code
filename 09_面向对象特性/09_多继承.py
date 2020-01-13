class A():
    def aa(self):
        print("aa")


class B:
    def bb(self):
        print("bb")


# 多继承可以让子类对象，同时具有多个父类的属性和方法
class C(A, B):  # 多继承
    pass


# 创建子类对象
c = C()
c.aa()  # A 类方法
c.bb()  # B类方法
