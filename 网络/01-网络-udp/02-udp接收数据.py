import socket


def main():
    # 1. 创建套接字
    # AF_INET ipv4, SOCK_DGRAM upd
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定服务端本地信息
    localaddr = ("", 8989)  # 服务端端口
    udp_socket.bind(localaddr)  # 必须绑定服务端自己的ip以及port

    # 3. 接收数据
    recv_data = udp_socket.recvfrom(1024)  # 接收字节数
    # recv_data是一个元组(接收到的数据，(发送方的ip, port))
    recv_msg = recv_data[0]  # 接收的数据
    send_addr = recv_data[1]  # 发送方的地址信息

    # 4. 打印接收到的数据
    # print(recv_data)
    # utf-8解码
    print("%s:%s" % (str(send_addr), recv_msg.decode("utf-8")))
    # print("%s:%s" % (str(send_addr), recv_msg.decode("gbk")))  # win默认gbk编码

    # 5. 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
