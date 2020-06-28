# 打开文件
file1_read = open("./13_文件操作/README.txt")  # 只读打开
file1_write = open("./13_文件操作/README_副本.txt", "w")  # 只写打开

# 读 写
while True:
    # 读取一行内容
    text_line = file1_read.readline()

    # 判断是否读取到内容
    if not text_line:
        break
    file1_write.writelines(text_line)  # 连续write写多次是追加写

# 关闭
file1_read.close()
file1_write.close()
