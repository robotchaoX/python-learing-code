# raise 主动抛出异常


def input_password():
    # 1. 提示用户输入密码
    pwd = input("请输入密码：")

    # 2. 判断密码长度 >= 8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    # 3. 如果 < 8 主动抛出异常
    print("主动抛出异常")
    # 1> 创建异常对象 - 传入异常描述信息
    ex_len_error = Exception("---密码长度不够---")  # 创建异常对象，Exception是异常类
    # 2> 主动抛出异常
    raise ex_len_error


try:
    print(input_password())
# 捕获异常
except Exception as error:
    print(error)
# 没有异常执行
else:
    print("密码输入完成，没有异常")
# 无论是否异常都执行
finally:
    print("无论是否出现异常都会执行的代码")
