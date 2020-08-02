import socket
import re
import time


# 服务器处理客户端请求
# new_socket客户端socket，request请求的内容
def service_client(new_socket, request):
    """为这个客户端返回数据"""
    # 1.提取客户端请求的文件名
    request_lines = request.splitlines()  # 按行分割请求
    print(">"*20)
    print(request_lines)
    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])  # 正则匹配请求中的文件名
    if ret:
        file_name = ret.group(1)
        # print("*"*50, file_name)
        if file_name == "/":  # 默认/
            file_name = "/index.html"

    # 2.返回http格式的数据，给浏览器
    try:
        f = open("./web服务器/html" + file_name, "rb")  # code runner路径是整个文件夹
        # f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found-----"
        new_socket.send(response.encode("utf-8"))
        print("------file not found-----", file_name)
    else:
        # 响应内容
        html_content = f.read()
        f.close()
        response_body = html_content
        # 响应头
        response_header = "HTTP/1.1 200 OK\r\n"
        # 响应数据长度，长链接，浏览器知道上次响应结束
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        # 拼接http协议响应
        response = response_header.encode("utf-8") + response_body
        # 给客户端发送http响应
        new_socket.send(response)


def main():
    """单进程，单线程，非阻塞，短链接，简单服务器"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞

    client_socket_list = list()  # 建立链接的客户端列表
    while True:
        time.sleep(0.5)
        # 4. 等待新客户端的链接
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as ret:
            print("---没有新的客户端到来---")
            pass
        else:
            # 只要没有产生异常，那么也就意味着 来了一个新的客户端
            print("+++++++++新的客户端建立连接+++++++++")
            new_socket.setblocking(False)  # 设置套接字为非堵塞的方式
            client_socket_list.append(new_socket)  # 新的客户端加入列表

        # 遍历客户端列表
        for client_socket in client_socket_list:
            try:
                # 客户端socket有没有返回
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                # print(ret)
                print("----这个客户端没有发送过来数据----")
                pass
            else:
                print("-----recv没有异常,要么接收到数据，要么断开连接-----")
                if recv_data:  # 客户端发送过来数据
                    print("----客户端发送过来了数据-----")
                    # 每次处理发送完请求，不断开链接，长链接
                    service_client(client_socket, recv_data)
                else:  # 返回数据为空
                    # 客户端调用close导致了recv返回,返回数据为空
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
