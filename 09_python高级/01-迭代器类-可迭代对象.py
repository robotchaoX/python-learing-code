import time
# 可迭代
from collections import Iterable
# 迭代器
from collections import Iterator


# 迭代器类
class ClassIterator(object):
    # 初始化，
    def __init__(self, Classmate_obj):
        self.obj = Classmate_obj
        self.current_num = 0

    # 类对象成为可迭代的对象
    def __iter__(self):
        pass

    # 迭代对象next的值
    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            # 迭代结束，抛出异常，自动停止迭代
            raise StopIteration


# 可迭代的类对象
class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    # 如果想要一个对象称为一个　可以迭代的对象，即可以使用for，
    # 那么必须实现__iter__方法,返回值是迭代器
    def __iter__(self):
        # self用于初始化ClassIterator的参数,初始化ClassIterator
        return ClassIterator(self)


classmate = Classmate()
classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

# 判断是否是可以迭代的对象Iterable
print("判断classmate是否是可以迭代的对象:", isinstance(classmate, Iterable))

# 判断是否是迭代器Iterator
# 迭代器 = iter(可迭代对象)
classmate_iterator = iter(classmate)  # 迭代器
print("判断classmate_iterator是否是迭代器:", isinstance(classmate_iterator, Iterator))

# 迭代器的next值
print("迭代器的next值:", next(classmate_iterator))

print("------------------")

# 迭代器，可遍历，自动调用next
for stu in classmate:
    print(stu)
    time.sleep(1)
