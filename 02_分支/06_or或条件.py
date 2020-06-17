# 定义两个整数变量 python_score、c_score，编写代码判断成绩
py_score = 50
c_score = 80

# 要求只要有一门成绩 > 60 分就算合格
if py_score >= 60 or c_score >= 60:  # or
    print("考试通过")
else:
    print("考试失败")
