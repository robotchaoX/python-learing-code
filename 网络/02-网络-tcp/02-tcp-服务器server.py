import socket


def main():
    # 1. 创建套接字 socket
    # 套接字可以同时 收发数据，全双共
    # AF_INET ipv4, SOCK_STREAM tcp
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定服务器端口 bind
    localaddr = ("", 8989)  # 服务端端口
    tcp_server_socket.bind(localaddr)  # 必须绑定服务端自己的ip以及port

    # 3. 套接字监听链接 listen
    tcp_server_socket.listen(128)

    # 4. 等待客户端的链接 accept
    # new_client_socket, client_addr = tcp_server_socket.accept()
    connect_ret = tcp_server_socket.accept()
    # print(connect_ret)
    # connect_ret是一个元组(cfd套接字，(发送方的ip, port))
    new_client_socket = connect_ret[0]  # cfd套接字
    client_addr = connect_ret[1]  # 客户端地址
    print(client_addr)

    # 循环目的: 为同一个客户端 服务多次
    while True:

        # 接收客户端发送过来的数据
        client_msg = new_client_socket.recv(1024)
        # print(client_msg)
        print("客户端发送的请求是: %s" % client_msg.decode("utf-8"))

        # 如果recv解堵塞，那么有2种方式：
        # 1. 客户端发送过来数据
        # 2. 客户端调用close导致而了 这里 recv解堵塞
        if client_msg:
            # 4.响应客户端请求
            # 向客户端发送数据
            respond_data = "----服务器收到了: " + client_msg.decode("utf-8") + "!"
            # utf-8编码发送的数据
            new_client_socket.send(respond_data.encode("utf-8"))

        else:
            break

    # 关闭套接字
    # 关闭cfd套接字,关闭accept返回的套接字，断开这个客户端的链接
    new_client_socket.close()

    # 关闭lfd套接字,关闭监听套接字,将不能再次等待accept新客户端的到来
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
