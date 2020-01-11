for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用break退出了循环
    # else 下方的代码就不会被执
    print("完整遍历,中途break则不会执行else")

print("循环结束")
