# 导入随机工具包
# 注意：在导入工具包的时候，应该将导入的语句，放在文件的顶部
# 因为，这样可以方便下方的代码，在任何需要的时候，使用工具包中的工具
import random

# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input("请输入您要出的拳 石头（1）／剪刀（2）／布（3）："))

# 电脑 随机 出拳 —— 石头（1）／剪刀（2）／布（3）
computer = random.randint(1, 3)  # 双闭区间 [1,3]

# 显示
print("玩家选择的拳头是 %d - vs - 电脑出的拳是 %d" % (player, computer))

# 比较胜负,以玩家为中心分情况
# 1	石头 胜 剪刀
# 2	剪刀 胜 布
# 3	布  胜 石头
# if ( ()
#        or ()
#        or () ):
# 玩家胜   # ()括号内代码可任意换行     # \ 表示续行
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):  # 1玩家胜
    print("玩家胜")
# 平局
elif player == computer:  # 2平局
    print("平局")
# 其他的情况就是电脑获胜
else:  # 3电脑胜(其他)
    print("电脑胜")
