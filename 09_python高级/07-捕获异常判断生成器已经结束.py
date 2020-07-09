# 如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器的模板
def create_num(all_num):
    print("----1---")
    fib_a, fib_b = 0, 1  # 初值
    current_num = 0
    while current_num < all_num:
        print("----2---")
        # print(fib_a)
        # 有yield语句，就不再是函数，而是一个生成器
        yield fib_a  # 变成生成器
        print("----3---")
        fib_a, fib_b = fib_b, fib_a + fib_b  # 递推
        current_num += 1
        print("----4---")
    return "....end...."  # 返回异常时value


# 创建生成器对象
obj2 = create_num(10)

while True:
    try:
        # next生成数据
        ret = next(obj2)
        print(ret)
    # 捕获生成器异常
    except Exception as ret:
        print(ret.value)
        break
