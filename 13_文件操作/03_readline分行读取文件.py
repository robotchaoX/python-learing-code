# readline()一次读取一行
# 打开文件
file1 = open("./13_文件操作/README.txt", "r")
while True:
    # 读取文件
    text1 = file1.readline()  # 分行读取
    # 读取的内容包含\n换行符 123456789\n

    # 判断是否读取到内容
    # 读取到内容末尾退出(空行是\n ,不是空)
    if not text1:
        break
    print(text1)  # print自动换行
    print(text1)

# 关闭文件
file1.close()


# readlines()按照行的方式一次性读取整个文件,返回列表,每行数据为一个元素
# 打开文件
file1 = open("./13_文件操作/README.txt", "r")
# readlines按行一次性读取整个文件
text_list = file1.readlines()
print(text_list)  # 列表
# 关闭文件
file1.close()
