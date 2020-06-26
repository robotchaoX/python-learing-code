# 自定义异常
# 继承异常类Exception


class WeakPwdExcept(Exception):
    # 有参构造
    def __init__(self, length, min_len, des_str):
        self.length = length
        self.min_len = min_len
        self.des_str = des_str

    # 抛出异常的描述信息
    def __str__(self):
        return "%s: 你输入的长度%d,小于最小值%d,不符合" \
            % (self.des_str, self.length, self.min_len)


def input_password():
    # 1. 提示用户输入密码
    pwd = input("请输入密码：")

    # 2. 判断密码长度 >= 8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    # 3. 如果 < 8 主动抛出异常
    print("主动抛出异常")
    # 1> 创建自定义异常对象 - 传入参数
    ex_len_error = WeakPwdExcept(len(pwd), 8, "---密码长度不够---")
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
