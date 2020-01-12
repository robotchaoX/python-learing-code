# 计算1+2+3+...num
def sum_numbers(num):
    # 出口
    if num == 1:
        return 1
    # 前num-1累加和
    # 假设 sum_numbers 能够正确的处理 1...num - 1
    temp = sum_numbers(num - 1)
    return num + temp


result = sum_numbers(100)
print(result)
