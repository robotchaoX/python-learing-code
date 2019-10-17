# 0~100偶数累加和
i = 0
result = 0
while i <= 100:
    # print(i)
    if i % 2 == 0:  # 偶数
        print(i)
        result += i
    i += 1
print("0~100偶数累加和 = %d" % result)
