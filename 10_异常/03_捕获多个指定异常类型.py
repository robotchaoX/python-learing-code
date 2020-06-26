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
    print(1/0)
except NameError:
    print("NameError异常")
# 捕获多个异常
except (ZeroDivisionError, ValueError):  # 多个异常 元组
    print("有错误")
