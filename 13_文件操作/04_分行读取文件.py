# 打开文件
file1 = open("README")

while True:
    # 读取文件
    text1 = file1.readline()  # 分行读取

    # 判断是否读取到内容
    # 读取到内容末尾退出(空行是\n ,不是空)
    if not text1:
        break
    print(text1)

# 关闭文件
file1.close()
