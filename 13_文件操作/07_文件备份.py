# 备份文件名
old_file_name = "./13_文件操作/README.txt"
# 拼接备份文件名
pt_index = old_file_name.rfind(".")
new_file_name = old_file_name[:pt_index]+"[备份]"+old_file_name[pt_index:]
# 打开文件
old_file = open(old_file_name, "rb")  # 只读打开
new_file = open(new_file_name, "wb")  # 只写打开

# 读 写
while True:
    # 每次读取固定长度
    text_line = old_file.read(1024)
    # 读取一行内容
    # text_line = old_file.readline()

    # 判断是否读取到内容
    if len(text_line) == 0:
        break
    new_file.write(text_line)  # 连续write写多次是追加写

# 关闭
old_file.close()
new_file.close()
