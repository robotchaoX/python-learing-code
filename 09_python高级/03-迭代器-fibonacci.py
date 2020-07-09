

# 生成斐波那契数列的列表
def fibo_fun():
    # 斐波那契结果列表
    fibo_list = list()

    a = 0
    b = 1
    i = 0
    while i < 10:
        # 列表存斐波那契结果
        fibo_list.append(a)
        a, b = b, a+b  # 递推
        i += 1

    # 斐波那契数列
    print(fibo_list)

    # # 遍历列表，斐波那契数列
    # for num in fibo_list:
    #     print(num)


# 调用函数
fibo_fun()


print("------------------")


# 迭代器生成斐波那契数列
class Fibonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            # 生成斐波那契数列，返回结果，不保存到列表
            ret = self.a
            self.a, self.b = self.b, self.a+self.b  # 递推
            self.current_num += 1
            return ret
        else:
            raise StopIteration


# 可迭代类对象
fibo = Fibonacci(10)


# 遍历时一个个生成斐波那契数列
# 遍历可迭代对象，自动调用next
for num in fibo:
    print(num)
