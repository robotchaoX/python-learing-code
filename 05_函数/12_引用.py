# python中，赋值是靠引用来传递的
# 数据能够直接修改就是可变类型,不能直接修改就是不可变类型
# 不可变类型（整型int、浮点型float、字符串str、元组tuple）
# 可变类型（列表list、字典dict、集合set）


# 1.不可变类型，赋值传引用
# int
a = 1  # a指向不可变量1
b = a  # 传引用，b也指向不可变量1
# a b 内存地址相同
print(a, id(a))  # 94833405678016
print(b, id(b))  # 94833405678016

# a重新赋值
a = 2  # a重新指向不可变量2
print(a, id(a))  # 94833405678048
# b依然指向不可变量1
print(b, id(b))  # 94833405678016

# += 数值
nums = 5
print(nums, id(nums))
nums += nums  # num 新同名局部变量???
print(nums, id(nums))


# 2.可变类型
# 列表list
aa_list = [44, 55]  # aa_list指向可变类型列表[44, 55]
bb_list = aa_list  # 传引用，bb_list也指向可变类型列表[44, 55]
# aa_list bb_list 内存地址相同
print(aa_list, id(aa_list))  # 140379902232520
print(bb_list, id(bb_list))  # 140379902232520
# 2.1append方法修改aa_list可变类型变量列表的数据,[44, 55, 66]
# aa_list地址不变
aa_list.append(66)  # aa_list追加数据
print(aa_list, id(aa_list))  # 140379902232520
# bb_list地址不变
print(bb_list, id(bb_list))  # 140379902232520

# 2.2aa_list重新赋值
aa_list = [77, 88]  # aa_list重新指向可变量列表[77, 88]
print(aa_list, id(aa_list))  # 140379902232456
# bb_list依然指向可变类型列表[44, 55, 66]
print(bb_list, id(bb_list))  # 140379902232520


# 列表地址不变
# += 列表
# 列表的 += 等价extend方法,地址不变,不是list=list+list,与数值不一样
num_list = [3, 4]
print("id=", id(num_list), ' val=', num_list)
num_list += num_list  # 等价extend方法
# num_list.extend(num_list) # 等价 +=
print("id=", id(num_list), ' val=', num_list)

# 列表地址改变
val = [3, 4]
print("id=", id(val), ' val=', val)
val = [5, 6, 7]  # 定义了同名变量??
val = val + [10]  # 重新定义同名变量??
# 列表的 += 等价extend方法,不是list=list+list,与数值不一样
val = val + val  # 新建同名局部变量,不影响实参???
val = val * 3  # 新建同名局部变量,不影响实参
print("id=", id(val), ' val=', val)


# 传参传变量的引用
def test(num):
    # 与传入地址相同
    print("---传入函数内部形参 %d 的地址 id(num) = %d" %
          (num, id(num)))  # 数值10的地址


# int 不可变类型
# 1. 定义一个数字的变量
a = 10  # 数据10 是单独存储的
print("实参变量 %d 的地址 id(a) = %d" % (a, id(a)))  # 数值10的地址

# 2. 调用函数，本质上传递的是实参保存数据的引用，而不是实参保存的数据！
# 传入 数据10 的引用
test(a)


# str 字符串 不可变类型
# 返回变量的引用
def test():
    # 1> 定义一个要返回的字符串变量
    result = "hello"  # "hello" 是单独存储的
    print("返回数据 %s 的地址 id(result) = %d" %
          (result, id(result)))  # 140573082855496

    # 2> 将字符串变量返回，返回的是数据的引用，而不是数据本身
    return result  # 返回 "hello" 的引用


# 获取返回值
ret = test()
# 与传出地址相同
print("%s 的地址是 id(ret) = %d" % (ret, id(ret)))  # 140573082855496
