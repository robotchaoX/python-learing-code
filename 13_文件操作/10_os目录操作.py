# 导入os模块
import os


# 目录操作

# rmdir 删除目录
# os.rmdir(目录名)
os.rmdir("newdir")

# mkdir 创建目录
# os.mkdir(目录名)
os.mkdir("olddir")

# rename 重命名文件夹/文件
# os.rename(源文件名, 目标文件名)
os.rename("olddir", "newdir")

# listdir 列出目录下的所有文件/目录
# os.listdir(目录名)
dir_list = os.listdir("./")
print(dir_list)

# path.isdir 判断是否是文件
# os.path.isdir(文件路径)
res = os.path.isdir("./13_文件操作")
print(res)

# chdir 修改工作目录
# os.chdir(目标目录)
os.chdir("/home")

# getcwd 获取当前目录
cwd = os.getcwd()
print(cwd)
