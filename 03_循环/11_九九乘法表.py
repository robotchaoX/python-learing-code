row = 1  # 行初值
while row <= 9:  # 条件
    col = 1  # 列初值
    while col <= row:  # 列
        # print("*", end="")
        print("%d * %d = %d" % (col, row, col * row), end="\t")  # 结束符为制表符
        col += 1
    # print("%d" % row)
    print("")
    row += 1  # 自增
