# 1 打开文件
file1 = open("README")

# 2 读取文件
text1 = file1.read()  # read读取文件后, 文件指针移动到末尾
print(text1)
print(len(text1))

print("-" * 50)

text1 = file1.read()
print(text1)  # 文件指针在末尾, 输出为空行
print(len(text1))

# 3 写入文件

# 4 关闭文件
file1.close()
