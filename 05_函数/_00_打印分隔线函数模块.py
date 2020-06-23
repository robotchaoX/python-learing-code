# 模块
# import导入函数模块时会从上向下执行
print("import导入函数模块开始...")

# 定义函数
def print_one_line(char):
    """
    函数说明：打印单行分隔线
    :param char: 分隔字符
    :param times: 重复次数
    """
    print(char * 10)


def print_mult_line(char, times):
    """
    函数说明：打印多行分隔线
    :param char: 分隔线使用的分隔字符
    :param times: 分隔线重复的次数
    """
    row = 0
    while row < 5:
        print_one_line(char)
        row += 1


# 定义变量
name = "我是模块变量"

print("import导入函数模块结束...")
