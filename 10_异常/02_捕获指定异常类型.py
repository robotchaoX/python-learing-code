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

try:
    num = int(input("输入一个整数:"))
    result = 8 / num
    print(result)
except ZeroDivisionError:  # 除0 异常
    print("除0错误")
except ValueError:  # int 异常
    print("请输入正确的整数")
