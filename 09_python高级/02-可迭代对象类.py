# 可迭代
# from collections import Iterable
# 迭代器
# from collections import Iterator
import time


# 可迭代的类对象
# __iter__,__next__
class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def addStu(self, name):
        self.names.append(name)

    # 如果想要一个对象称为一个　可以迭代的对象，即可以使用for，
    # 那么必须实现__iter__方法,返回值是迭代器
    def __iter__(self):
        # 调用iter(xxobj)的时候 只要__iter__方法返回一个 迭代器即可，至于是自己 还是 别的对象都可以的, 但是要保证是一个迭代器(即实现了 __iter__  __next__方法)
        return self

    # 每次迭代自动调用__next__
    # 迭代对象next的值
    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            # 迭代结束，抛出异常，自动停止迭代
            raise StopIteration


classmate = Classmate()
classmate.addStu("老王")
classmate.addStu("王二")
classmate.addStu("张三")

# # 判断是否是可以迭代的对象Iterable
# print("判断classmate是否是可以迭代的对象:", isinstance(classmate, Iterable))
# # 判断是否是迭代器Iterator
# # 迭代器 = iter(可迭代对象)
# classmate_iterator = iter(classmate)  # 迭代器
# print("判断classmate_iterator是否是迭代器:", isinstance(classmate_iterator, Iterator))
# # 迭代器的next值
# print("迭代器的next值:", next(classmate_iterator))
# print("------------------")


# 遍历可迭代对象，自动调用next
for stu in classmate:
    print(stu)
    time.sleep(1)
