# open打开文件
# open(path,mode)
# 相对路径,(python终端)
# file1 = open("./13_文件操作/README.txt")
# 绝对路径
# file1 = open("/home/chao/Documents/Python/python-learning-code/13_文件操作/README.txt")


# 打开文件模式
# r 只读(默认,保留), w 只写(清空), a 追加
# r+读写(文件指针在开头,保留), w+读写(文件指针在开头,清空), a+追加(文件指针在末尾,追加)
# rb二进制读, rb+二进制读写, wb二进制只写, wb+二进制读写

# 默认 r 只读(默认)
# file1 = open("./13_文件操作/README.txt")

# r 只读(默认),如果文件不存在,报错
# file1 = open("./13_文件操作/README.txt", "r")

# w 只写(覆盖),如果文件不存在,新建文件;如果文件存在,清空源内容
# file1 = open("./13_文件操作/README.txt", "w")

# a 追加 如果文件不存在,新建文件
# file1 = open("./13_文件操作/README.txt", "a")


# r+ 读写(文件指针在开头),如果文件不存在,报错
# file1 = open("./13_文件操作/README.txt", "r+")

# w+ 读写(文件指针在开头,清空),如果文件不存在,新建文件;如果文件存在,清空源内容
# file1 = open("./13_文件操作/README.txt", "w+")

# a+ 追加(文件指针在末尾,追加),如果文件不存在,新建文件
# file1 = open("./13_文件操作/README.txt", "a+")


# 关闭文件
# file1.close()
