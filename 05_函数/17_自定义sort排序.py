# 自定义sort排序
# sort(key=lambda...,reverse=True)

student = [
    {"name": "Tom", "age": 18},
    {"name": "Rose", "age": 22},
    {"name": "Jack", "age": 16},
]

# 按照字典的键key排序
# 按字典的键 "name"对应的值升序排序
student.sort(key=lambda x: x["name"])
print(student)
# 按字典的键 "age"对应的值升序排序
student.sort(key=lambda x: x["age"])
print(student)


# 按字典的键 "name"对应的值降序排序
student.sort(key=lambda x: x["name"], reverse=True)
print(student)
# 按字典的键 "age"对应的值降序排序
student.sort(key=lambda x: x["age"], reverse=True)
print(student)
