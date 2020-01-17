import message_pck

message_pck.send_message.send("hello")

txt = message_pck.receive_message.receive()
print(txt)
