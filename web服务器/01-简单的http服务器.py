import socket


# 服务器接收请求，处理，响应
def service_client(new_socket):
    """为这个客户端返回数据"""
    # 1. 接收浏览器发送过来的http请求
    # GET / HTTP/1.1
    # .....
    request = new_socket.recv(1024).decode("utf-8")  # 解码

    # 2. 处理http请求
    print("------------------request-------------------")
    print(request)

    # 3. 给浏览器发送http格式的响应数据
    # 3.1拼接发送给浏览器的http格式数据---http-header
    response = "HTTP/1.1 200 OK\r\n"  # 响应行
    response += "Content-Type: html;charset=utf-8\r\n"  # 响应头
    response += "\r\n"  # 空行
    # 3.2拼接发送给浏览器的http格式数据---http-body
    response += "This is response..."  # 响应数据
    # 3.3发送响应
    new_socket.send(response.encode("utf-8"))

    # 4. 关闭套接字
    new_socket.close()


# 浏览器打开 http://127.0.0.1:7890
def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置套接字选项(可选)
    # 即使服务器先关闭也不需要等2MSL时间(谁先close关闭谁等待2MSL时间)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定端口
    tcp_server_socket.bind(("", 7890))  # 服务器端口

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        service_client(new_socket)

    # 6.关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
