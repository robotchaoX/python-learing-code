"""
__title__ = ''
__author__ = 'chao'
__mtime__ = '18-12-5'
__version__=''
__packages__=''
__description__=''
"""


# 定义Gun类
class Gun():
    def __init__(self, model):  # 定义属性
        # 1 枪型号
        self.model = model

        # 2 子弹数量
        self.bullet_count = 0  # 定义属性时初始子弹数量为0

    def add_bullet(self, count):  # 定义方法
        self.bullet_count += count

    def shoot(self):
        # 1 判断子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了..." % self.model)
            return
        # 2 子弹-1
        self.bullet_count -= 1
        # 3 发射提示信息
        print("[%s]突突突... 剩余[%d]子弹" % (self.model, self.bullet_count))


# 定义Soldier
class Soldier():
    def __init__(self, name):  # 定义属性
        self.name = name
        self.gun = None  # 定义属性时初始值为空,None可以赋值给任何变量


# 创建Gun对象ak47
ak47 = Gun("AK47")
print(ak47)
ak47.add_bullet(50)
ak47.shoot()

# 创建Soldier对象
xusanduo = Soldier("许三多")
xusanduo.gun = ak47  # 一个对象可作为另一对象的属性(对象可嵌套)
print(xusanduo)

"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃   神兽保佑   ┣┓
                ┃ 　永无BUG！  ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
