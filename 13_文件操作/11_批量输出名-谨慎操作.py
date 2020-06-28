# 导入os模块
import os

# 文件夹名添加 python_ 前缀

# 当前路径的所有文件夹
dir_list = os.listdir("./")
print(dir_list)

# 遍历文件夹列表
for dir_name in dir_list:
    # 构造新名字
    newName = "python_" + dir_name  # 拼接
    # 重命名
    os.rename(dir_name, newName)


print("----------------------")


# 删除文件夹名 python_ 前缀

# 当前路径的所有文件夹
dir_list = os.listdir("./")
print(dir_list)

# 遍历文件夹列表
for dir_name in dir_list:
    # 构造新名字
    beg = len("python_")
    newName = dir_name[beg:]  # 切片
    # 重命名
    os.rename(dir_name, newName)
