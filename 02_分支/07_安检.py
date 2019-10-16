has_ticket = True
knife_length = 22
if has_ticket:
    print("有票")
    if knife_length >= 30:
        print("安检未通过,刀的长度是%d" % knife_length)
    else:
        print("安检通过")

else:
    print("请买票")
