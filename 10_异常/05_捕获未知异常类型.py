# 异常处理
# try:
#     可能错误的代码
# except 异常类型:
#     处理异常
# else:
#     没有异常执行
# finally:
#     无论是否异常都执行


# Exception 是所有程序异常类的父类

try:
    num = int(input("输入一个整数:"))
    result = 8 / num
    print(result)
# 指定异常类型
except ZeroDivisionError:  # 除0 异常
    print("除0错误")
# Exception 所有异常
except Exception as error:  # 未知异常
    print("未知错误: %s" % error)
