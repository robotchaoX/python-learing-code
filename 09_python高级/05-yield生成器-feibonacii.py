# 生成器是特殊的迭代器
# yield


# 如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器的模板
def create_num(all_num):
    print("----1---")
    fib_a, fib_b = 0, 1  # 初值
    current_num = 0
    while current_num < all_num:
        print("----2---")
        # print(fib_a)
        # 有yield语句，就不再是函数，而是一个生成器的模板
        yield fib_a  # 变成生成器
        print("----3---")
        fib_a, fib_b = fib_b, fib_a + fib_b  # 递推
        current_num += 1
        print("----4---")


print("--------obj1----------")


# 如果在调用create_num的时候，发现这个函数中有yield那么此时，
# 不是调用函数，而是创建一个生成器对象
gen_obj = create_num(10)  # 创建生成器对象
# next生成数据
ret = next(gen_obj)
print(ret)
# next生成数据
ret = next(gen_obj)
print(ret)


print("--------obj2----------")


# 创建生成器对象
gen_obj_2 = create_num(2)  # 总数2

# next生成数据
# 1
ret = next(gen_obj_2)
print(ret)
# 2
ret = next(gen_obj_2)
print(ret)
# 3
# 次数超额，产生异常
# ret = next(gen_obj_2)
# print(ret)


print("--------obj3----------")


# 创建生成器对象
gen_obj_3 = create_num(2)

# 生成器是特殊的迭代器，可遍历，自定调用next
for num in gen_obj_3:
    print(num)
