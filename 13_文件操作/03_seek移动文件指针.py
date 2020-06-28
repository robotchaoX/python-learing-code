# seek() 移动文件指针  起始位置:0开头,1当前,2结尾
# 文件对象.seek(偏移量,起始位置)

# 打开文件
file1 = open("./13_文件操作/README.txt", "r+")

# 偏移量4,起始0开头
# 起始位置:0开头, 1当前, 2结尾
file1.seek(4, 0)  # 文件指针从开头偏移4字节

# 文件指针移到结尾
# file1.seek(0, 2)  # 起始位置:2结尾

# 文件指针移到开头
# file1.seek(0, 0)  # 起始位置:0开头
# file1.seek(0)  # 简写

# 读入
text1 = file1.read()  # read默认读取所有内容(从当前文件指针)
print(text1)  # w+ a+方式打开的,读入为空?
print(len(text1))

# 关闭
file1.close()
