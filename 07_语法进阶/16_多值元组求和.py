def sum_numbers(args_tuple):  # 直接传递元组
    num = 0
    print(args_tuple)
    for num in args_tuple:
        num += num
    return num


result = sum_numbers((1, 2, 3))  # 直接传递元组
print(result)


def sum_numbers(*args):  # 多值参数传递元组
    num = 0
    print(args)

    # for遍历
    for n in args:
        num += n
    return num


result = sum_numbers(1, 2, 3)  # 多值参数传递元组
print(result)
