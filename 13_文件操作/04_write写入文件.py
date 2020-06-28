# 打开文件模式
# r 只读(默认,保留), w 只写(清空), a 追加
# r+读写(文件指针在开头,保留), w+读写(文件指针在开头,清空), a+追加(文件指针在末尾,追加)
# rb二进制读, rb+二进制读写, wb二进制只写, wb+二进制读写

file1 = open("./13_文件操作/README.txt", "r+")

# 读入
txt_line = file1.readline()  # 包含换行符\n
print(txt_line)  # print自动换行,内容包含\n,所以有空行
text1 = file1.read()  # read读取所有内容(从当前文件指针)
print(text1)  # w+ a+方式打开的,读入为空?
print("读取的字节数", len(text1))

# 写入,可以使用 转义字符 \n
# 连续write写是追加
file1.write("123 hello")
file1.write("456 hello")  # 同一行
file1.write("\n123456写入")  # \n换行
file1.write("\n789写入")

# 关闭
file1.close()
