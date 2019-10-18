def print_(char_, num_):
    """说明
    :param char_: 分隔符
    :param num_: 重复次数
    """
    print(char_ * num_)


def print_line(char_, num_):
    """打印多行
    :param char_: 分隔符
    :param num_: 重复次数
    """
    row = 0
    while row < 5:
        print_(char_, num_)
        row += 1


print_line("++", 50)
