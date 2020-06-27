# 导入包下的模块
# 包名.模块名
import message_pck.send_message
import message_pck.receive_message

# 调用包中的函数
# 包名.模块.函数
message_pck.send_message.send("hello")

txt = message_pck.receive_message.receive()
print(txt)
