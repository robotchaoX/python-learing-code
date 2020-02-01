# 打开文件
file1_read = open("README")  # 只读打开
file1_write = open("readme_副本", "w")  # 只写打开

# 读 写
text = file1_read.read()
file1_write.write(text)

# 关闭
file1_read.close()
file1_write.close()
