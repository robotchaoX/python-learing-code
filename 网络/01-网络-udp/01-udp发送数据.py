# socket
import socket


def main():
    # 创建一个udp套接字
    # AF_INET ipv4, SOCK_DGRAM upd
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # # 绑定本地信息，不绑定则随机分配端口(可选)
    # udp_socket.bind(("", 1234))

    # 使用套接字收发数据
    # udp_socket.sendto("发送的数据", 对方的ip以及port元组)
    # 服务端 IP+port
    server_addr = ("192.168.0.18", 8989)
    send_data = "----utf-8 你好啊哈哈哈 utf-8----"
    # utf-8编码
    udp_socket.sendto(send_data.encode("utf-8"), server_addr)
    # bytes编码ASCII
    udp_socket.sendto(b"----ASCII I am udp ASCII----", server_addr)
    # TypeError: a bytes-like object is required, not 'str'
    # b：bytes can only contain ASCII literal characters

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
