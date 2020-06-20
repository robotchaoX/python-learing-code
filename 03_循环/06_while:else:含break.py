i = 0
while i < 5:
    # break 某一条件满足时，退出循环，不再执行后续重复的代码
    if i == 3:
        break
    print(i)
    i += 1
# while正常结束循环才会执行else语句,否则跳过,不执行,
# while中间有break退出,则不执行else语句
# while中间有continue是正常结束,执行else语句
else:
    # 3. 正常结束循环才会执行else语句
    print("正常结束循环才会执行else语句，i = %d" % i)

# 4. 观察一下，循环结束后，计数器 i 的数值是多少
print("break退出,不执行else, i = %d" % i)
