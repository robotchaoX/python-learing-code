# 仅定义函数,不会执行
def multiple_table():  # def 函数定义也需要 :
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # print("*", end="")
            print("%d * %d = %d" % (col, row, col * row), end="\t")
            col += 1
        print("")
        row += 1

# 仅定义函数,啥也不执行
