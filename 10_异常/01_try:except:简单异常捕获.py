# 异常处理
# try:
#     可能错误的代码
# except 异常类型:
#     处理异常
# else:
#     没有异常执行
# finally:
#     无论是否异常都执行

# 异常类型
# NameError: 名字异常,未定义
# print(num)

# ZeroDivisionError: 除0异常
# print(1/0)


try:  # 可能错误的代码
    num = int(input("请输入一个整数:"))
# 捕获异常
# except  :  # 默认任意异常
except ValueError:  # 指定异常类型
    print("请输入正确的整数")

print("-" * 50)
