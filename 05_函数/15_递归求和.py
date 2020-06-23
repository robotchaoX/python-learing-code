

# 计算1+2+3+...num
def sum_numbers(num):
    # 递归的出口，当参数满足某个条件时，不再执行函
    if num == 1:
        return 1

    # 假设 sum_numbers 能够正确的处理 1...num-1
    # 即:前 num-1 累加和 的结果
    temp = sum_numbers(num - 1)  # 递归 # 自己调用自己
    return num + temp  # 返回结果


# 递归求和
result = sum_numbers(100)
print(result)


# 全局变量
result = 0


# 计算1+2+3+...num
def sum_numbers(num):
    global result
    # 递归的出口，当参数满足某个条件时，不再执行函
    if num == 1:
        return 1

    # 假设 sum_numbers 能够正确的处理 1...num-1
    # 即:前 num-1 累加和 的结果
    temp = sum_numbers(num - 1)  # 递归 # 自己调用自己
    result = num + temp
    return result


# 递归求和
sum_numbers(100)
print(result)
