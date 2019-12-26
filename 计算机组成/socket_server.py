import socket
import time
import threading
import errno


EOL1 = b'\n\n'
EOL2 = b'\n\r\n'

body = ''' Hello world <h1> 测试socket </h1> - from {thread_name}'''
response_params = [
    "HTTP/1.0 200 OK",
    "Date: Thu, 21 Nov 2019 03:17:57 GMT",
    "Content-Type: text/html; charset=utf-8",
    "Content-Length: {length}\r\n",
    body,
]
response = "\r\n".join(response_params)

def handle_connection(conn,addr):
    print(conn,addr)
    # time.sleep(3)
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    current_thread = threading.currentThread() 
    content_length = len(body.format(thread_name=current_thread.name).encode())
    print(current_thread.name)
    conn.send(response.format(thread_name=current_thread.name,length=content_length).encode())
    conn.close()

def main():
    # socket AF INET 用于服务器 服务器之间的 网络通信
    # socket SOCK_STREAM 用于 TCP 流式 socket 通信
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置端口可复用，保证每次按ctrl + c 键之后快速重启
    serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    serversocket.bind(("127.0.0.1",8000))
    serversocket.listen(10) # 设置backlog-socket 连接最大排队数量
    print("http://127.0.0.1:8000")
    serversocket.setblocking(0) # 设置socket为非阻塞模式

    try:
        i = 0
        while True:
            try:
                conn,address = serversocket.accept()
                handle_connection(conn,address)
            except BlockingIOError as e:
                continue
            except socket.error as e:
                if e.args[0] != errno.EAGAIN:
                    raise
                continue
            i += 1
            print(i)
            t = threading.Thread(target=handle_connection,args=(conn,address),name="thread-%s"%i)
            t.start()
    finally:
        serversocket.close()


if __name__ == "__main__":
    main()
