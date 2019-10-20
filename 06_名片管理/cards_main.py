#! /opt/anaconda3/bin/python3
#  #!符号叫shebang,指明脚本文件的解释器路径,可直接作为可执行脚本文件

import cards_tools

# 无限循环,由用户主动退出
while True:
    # TODO 显示菜单
    cards_tools.show_menu()

    action_str = input("请选择操作功能:")
    print("您选择的操作是: [%s] " % action_str, end="")

    # 1,2,3调用功能
    if action_str in ["1", "2", "3"]:
        # 1 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 2 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 3 查询名片
        elif action_str == "3":
            cards_tools.search_card()

        pass

    # 0 退出系统
    elif action_str == "0":
        print("退出[名片管理系统]")
        break

        pass  # 占位符

    # 其他,错误提示
    else:
        print("输入错误,请重新输入:")
