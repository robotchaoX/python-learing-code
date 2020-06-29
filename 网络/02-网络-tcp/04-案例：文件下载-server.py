import socket


def send_file_2_client(new_client_socket, client_addr):
    # 1. 接收客户端 需要下载的文件名
    # 接收客户端发送过来的 要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端(%s)需要下载文件是：%s" % (str(client_addr), file_name))

    file_content = None
    # 2. 打开这个文件，读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件(%s)" % file_name)

    # 3. 发送文件的数据给客户端
    if file_content:
        # new_client_socket.send("-----ok-----".encode("utf-8"))
        new_client_socket.send(file_content)


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

    while True:
        # 4. 等待客户端的链接 accept
        # new_client_socket, client_addr = tcp_server_socket.accept()
        connect_ret = tcp_server_socket.accept()
        # print(connect_ret)
        # connect_ret是一个元组(cfd套接字，(发送方的ip, port))
        new_client_socket = connect_ret[0]  # cfd套接字
        client_addr = connect_ret[1]  # 客户端地址
        # print(client_addr)

        # 5. 调用发送文件函数，完成为客户端服务
        send_file_2_client(new_client_socket, client_addr)

        # 6.关闭cfd套接字,关闭accept返回的套接字，断开这个客户端的链
        new_client_socket.close()

    # 7.关闭lfd套接字,关闭监听套接字,将不能再次等待accept新客户端的到来
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
