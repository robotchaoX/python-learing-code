try:
    num = int(input("输入一个整数:"))
    result = 8 / num
    print(result)
except ZeroDivisionError:  # 除0 异常
    print("除0错误")
except Exception as error:  # 未知异常
    print("未知错误: %s" % error)
else:  # 没有异常执行
    print("尝试成功，没有异常")
finally:  # 无论是否异常都执行
    print("无论是否出现异常都会执行的代码")

print("-" * 50)
