# 行与缩进
# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {}
if True:
    print("True")
else:
    print("False")
    print("False")
print("缩进决定代码执行顺序")

# 多行语句换行(与c++相同)
# Python 如果语句很长，我们可以使用反斜杠\来实现多行语句换行
total = 'item_one' + \
    'item_two' + \
    'item_three'

# 在 [], {}, 或 () 中的多行语句,不需要使用反斜杠(\),直接换行
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']
