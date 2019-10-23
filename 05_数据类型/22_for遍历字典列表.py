student = [
    {"name": "阿土"},
    {"name": "小美"}
]
find_name = "张三"
for stu_dict in student:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 %s " % find_name)
        break
else:
    print("没找到 %s " % find_name)

print("循环结束")
