# 函数文档
# 函数的返回值，不需要说明，直接return


def sum_2_num(num1, num2):
    """这是说明文档：对两个数字的求和"""
    result = num1 + num2
    # 可以使用返回值，告诉调用函数一方计算的结果
    return result


# help查看函数说明文档,q退出
# help(len)
help(sum_2_num)


def min_2_num(num1, num2):
    """
    这是说明文档：对两个数字的求和
    :param num1: 参数1
    :param num2: 参数2
    """
    result = num1 - num2
    # 可以使用返回值，告诉调用函数一方计算的结果
    return result


# help查看函数说明文档,q退出
# 参数说明
help(min_2_num)
