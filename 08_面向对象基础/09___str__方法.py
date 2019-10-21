"""
__title__ = ''
__author__ = 'chao'
__mtime__ = '18-12-3'
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
                ┃　 永无BUG！  ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

class Cat():
    def __init__(self, new_name):
        self.name = new_name
        print("%s 我来了" % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)

    def __str__(self):
        return "print(对象)时 __str__ return: 我是小猫 %s" % self.name


tom = Cat("Tom猫")
print(tom)


