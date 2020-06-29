import socket


def main():
    # 1. 创建套接字
    # 套接字可以同时 收发数据，全双共
    # AF_INET ipv4, SOCK_DGRAM upd
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定服务器端口 bind
    localaddr = ("", 8989)  # 服务端端口
    udp_socket.bind(localaddr)  # 必须绑定服务端自己的ip以及port

    while True:
        # 3. 接收客户端数据
        client_data = udp_socket.recvfrom(1024)  # 接收字节数
        # print(recv_data)
        # recv_data是一个元组(接收到的数据，(发送方的ip, port))
        client_msg = client_data[0]  # 接收的数据
        client_addr = client_data[1]  # 发送方的地址信息
        # utf-8解码接收到的数据
        print("客户端地址：%s,数据:%s" % (str(client_addr), client_msg.decode("utf-8")))
        # print("%s:%s" % (str(client_addr), client_msg.decode("gbk")))  # win默认gbk编码

        # 4.响应客户端请求
        # 向客户端发送数据
        # 客户端 IP+port
        client_addr = client_addr
        send_data = "----服务器收到了:" + client_msg.decode("utf-8") + "!"
        # utf-8编码发送的数据
        udp_socket.sendto(send_data.encode("utf-8"), client_addr)

    # 5. 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
