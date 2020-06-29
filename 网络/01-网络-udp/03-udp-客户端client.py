import socket


def main():
    # 1.创建一个udp套接字
    # 套接字可以同时 收发数据，全双共
    # AF_INET ipv4, SOCK_DGRAM upd
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # # 2.绑定本地信息，不绑定则随机分配端口(可选)
    # udp_socket.bind(("", 1234))  # 客户端自己的发送端口

    while True:
        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")
        # 如果输入的数据是exit，那么就退出程序
        if send_data == "exit":
            break

        # 3.向服务器发送数据
        # udp_socket.sendto("发送的数据", 对方的ip以及port元组)
        # 服务端 IP+port
        server_addr = ("192.168.0.18", 8989)
        # send_data = "----utf-8 你好啊哈哈哈 utf-8----"
        # utf-8编码发送的数据
        udp_socket.sendto(send_data.encode("utf-8"), server_addr)

        # 套接字可以同时 收发数据，全双共

        # 4.接收服务器的响应的数据
        server_data = udp_socket.recvfrom(1024)
        # print(server_data)
        # server_data是一个元组(接收到的数据，(发送方的ip, port))
        server_msg = server_data[0]  # 接收的数据
        server_addr = server_data[1]  # 发送方的地址信息,实际同上
        # utf-8解码接收到的数据
        print("服务器响应地址：%s,数据:%s" %
              (str(server_addr), server_msg.decode("utf-8")))

    # 5.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
