import socket
import re
# epoll库
import select


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

    # 2. 返回http格式的数据，给浏览器
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


# 浏览器打开 http://127.0.0.1:7890
def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))
    print("prot:7890")

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(),
                 select.EPOLLIN)  # .fileno()文件描述符，EPOLLIN监听读事件

    fd_event_dict = dict()  # 记录被监听的客户端的{fd文件描述符：socket套接字}对应关系

    while True:
        # 默认会堵塞，直到 os监测到数据到来 通过事件通知方式 告诉这个程序，此时才会解堵塞
        # 返回有监听事件的socket列表[(fd1, event1),(fd2, event2),(fd3, event3)]
        fd_event_list = epl.poll()  # 阻塞等待事件
        # 遍历返回的事件列表
        # [(fd1, event1),(fd2, event2),(fd3, event3)]  # (fd套接字对应的文件描述符,event监听的事件)
        for fd, event in fd_event_list:
            # lfd监听套接字的事件，为新客户端建立链接
            if fd == tcp_server_socket.fileno():
                # 新客户端建立链接
                new_socket, client_addr = tcp_server_socket.accept()
                print("+++++++++新的客户端建立连接+++++++++")
                # 添加到epoll进行监听
                epl.register(new_socket.fileno(), select.EPOLLIN)
                # 被监听的客户端的{文件描述符：socket}字典，记录对应关系
                fd_event_dict[new_socket.fileno()] = new_socket
            # 已连接客户端的事件，收发数据/断开链接
            elif event == select.EPOLLIN:
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                # 判断已经链接的客户端是否有数据发送过来
                # 客户端发送过来数据
                if recv_data:
                    print("----客户端发送过来了数据-----")
                    # 每次处理发送完请求，不断开链接，长链接
                    service_client(fd_event_dict[fd], recv_data)
                # 客户端调用close,返回数据为空
                else:
                    fd_event_dict[fd].close()
                    print("+++++++++客户端已经关闭+++++++++")
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
