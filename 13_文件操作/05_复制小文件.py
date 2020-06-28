# 打开文件
file1_read = open("./13_文件操作/README.txt")  # 只读打开
file1_write = open("./13_文件操作/README_副本.txt", "w")  # 只写打开

# 读 写
# read读取全部
text = file1_read.read()
# write写全部
file1_write.write(text)

# 关闭
file1_read.close()
file1_write.close()
