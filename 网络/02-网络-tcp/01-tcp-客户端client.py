import socket


def main():
    # 1. 创建tcp的套接字
    # AF_INET ipv4, SOCK_STREAM tcp
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # # 2.绑定本地信息，不绑定则随机分配端口(可选)
    # tcp_socket.bind(("", 1234))  # 客户端自己的发送端口

    # 2. 链接服务器
    # server_ip = input("请输入要链接的服务器的ip:")
    # server_port = int(input("请输入要链接的服务器的port:"))
    # server_addr = (server_ip, server_port)
    # 服务器地址
    server_addr = ("192.168.0.11", 8989)
    tcp_socket.connect(server_addr)

    # 循环发送
    while True:
        # 从键盘获取数据
        send_data = input("请输入要发送的数据:")
        # 如果输入的数据是exit，那么就退出程序
        if send_data == "exit":
            break

        # 3.向服务器发送数据
        # utf-8编码发送的数据
        tcp_socket.send(send_data.encode("utf-8"))

        # 套接字可以同时 收发数据，全双共

        # 4.接收服务器的响应的数据
        server_msg = tcp_socket.recv(1024)
        # print(server_msg)
        # utf-8解码接收到的数据
        print("服务器响应数据: %s" % server_msg.decode("utf-8"))

    # 4. 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()
