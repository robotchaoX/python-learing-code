import socket
# 正则表达式
import re


# 服务器接收浏览器请求，处理，响应
def service_client(new_socket):
    """为这个客户端返回数据"""
    # 1. 接收浏览器发送过来的http请求
    # GET / HTTP/1.1
    # .....
    request = new_socket.recv(1024).decode("utf-8")  # 解码

    # 2. 处理http请求
    print("------------------request-------------------")
    print(request)
    # 按行切分字符串splitlines
    request_lines = request.splitlines()  # 按行存入列表
    # print("--------splitlines----------")
    # print(request_lines)
    # 正则匹配请求的文件名
    # GET /index.html HTTP/1.1  # 请求行
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])  # 正则匹配文件名
    if ret:
        file_name = ret.group(1)
        print("..........浏览器请求文件：", file_name)
        if file_name == "/":  # 默认/
            file_name = "/index.html"

    # 3. 给浏览器发送http格式的响应数据
    try:
        # 3.0打开浏览器请求的文件
        f = open("./web服务器/html" + file_name, "rb")  # 二进制读(文件保存时的编码方式)
    except:
        # 打开文件失败，文件不存在
        response = "HTTP/1.1 404 NOT FOUND\r\n"  # 状态行
        response += "\r\n"  # 空行
        response += "------file not found-----"  # 响应数据
        # 发送404响应
        new_socket.send(response.encode("utf-8"))
    else:
        # 打开文件成功
        # 3.2拼接发送给浏览器的http格式数据---http-body
        # 从文件读取html响应数据
        html_content = f.read()  # 响应数据
        f.close()
        # 3.1拼接发送给浏览器的http格式数据---http-header
        response = "HTTP/1.1 200 OK\r\n"  # 状态行
        response += "\r\n"  # 空行
        # 3.3发送响应
        # 给浏览器发送响应头http-header
        new_socket.send(response.encode("utf-8"))
        # 给浏览器发送响应数据http-header
        new_socket.send(html_content)  # 二进制数据已经编码，不需要再编码

    # 关闭套接
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

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
