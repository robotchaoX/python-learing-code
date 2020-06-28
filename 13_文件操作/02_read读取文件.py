# 打开文件模式
# r 只读(默认,保留), w 只写(清空), a 追加
# r+读写(文件指针在开头,保留), w+读写(文件指针在开头,清空), a+追加(文件指针在末尾,追加)
# rb二进制读, rb+二进制读写, wb二进制只写, wb+二进制读写

# 1 open打开文件
# open(path,mode)
file1 = open("./13_文件操作/README.txt", "r")

# 2 read读取文件
# read不写参数,表示默认读取所有内容,
# text1 = file1.read()  # 默认读取全部内容
# 读取指定字节数
text1 = file1.read(5)  # 读取
print(text1)
print("读取的字节数", len(text1))


# 3 关闭文件
file1.close()


print("---------------")


# read读取文件后, 文件指针移动到末尾
# 1 打开文件
file1 = open("./13_文件操作/README.txt")

# 2 读取文件
# read默认读取全部内容
text1 = file1.read()  # read读取文件后,文件指针移动到末尾
print(text1)
print("读取的字节数", len(text1))

print("--------再次读取----------")

# 再次读取
text1 = file1.read()
print(text1)  # 文件指针在末尾, 输出为空行
print("读取的字节数", len(text1))

# 3 关闭文件
file1.close()
