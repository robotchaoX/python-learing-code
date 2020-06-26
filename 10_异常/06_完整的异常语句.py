# 异常处理
# try:
#     可能错误的代码
# except 异常类型:
#     处理异常
# else:
#     没有异常执行
# finally:
#     无论是否异常都执行


try:
    num = int(input("输入一个整数:"))
    result = 8 / num
    print(result)
except ZeroDivisionError:  # 除0 异常
    print("除0错误")
except (NameError, ValueError):  # 多个异常
    print("有错误NameError,ValueError")
except Exception as error:  # 未知异常
    print("未知错误: %s" % error)
# 没有异常执行
else:
    print("尝试成功，没有异常")
# 无论是否异常都执行
finally:
    print("无论是否出现异常都会执行的代码")

print("------------------")
