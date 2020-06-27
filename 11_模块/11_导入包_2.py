# 导入包下的所有模块
# 必须在包下__init__.py文件里设置__all__列表，添加允许导入的模块
# from 包名 import *
from message_pck import *  # ?? error

# 调用包中的函数
# 模块.函数
send_message.send("hello")

txt = receive_message.receive()
print(txt)
