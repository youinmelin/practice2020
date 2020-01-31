# 非堵塞方式单进程线程实现并发方法,并实现长链接
import re
import socket
import time

def handle_client(client_socket,recv_data):
#    recv_data = client_socket.recv(1024).decode('utf-8')
    print(recv_data)
    recv_data_list = recv_data.splitlines()
    # file_name
    ret = re.match(r"[^/]+(/[^ ]*)", recv_data_list[0])
    if ret:
        file_name = ret.group(1)
        if file_name == '/':
            file_name = '/index.html'
    else:
        file_name = '/index.html'
    print(file_name)
    response_body = read_file(file_name)
    if response_body == 'error':
        response_body = "404 not found"
        response_header = "HTTP/1.1 404 not found\r\n"
        response_header += "Content-Type: text/html; charset=utf-8\r\n"
        response_header += "Content-Length: %d\r\n" % (len(response_body))
        response_header += "\r\n"
        response = (response_header + response_body).encode('utf-8')
    else:
        response_header = 'HTTP/1.1 200 OK\r\n'
        response_header += 'Content-Length:%d\r\n'%len(response_body)
        #response_header += 'Content-Length:300\r\n'
        response_header += '\r\n'
        response = response_header.encode('utf-8') + response_body
        #response = response_header
    client_socket.send(response)
#    client_socket.close()

def read_file(file_name):
    try:
        with open ('./html'+file_name,'rb') as f:
            file_content = f.read()
    except Exception as e:
        file_content = 'error'
        print(e)
    return file_content

def main():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('',7890))
    server_socket.listen(128)
    client_socket_list = []
    server_socket.setblocking(False)  #设置套接字为非堵塞
    while True:
        try:
            client_socket,client_addr = server_socket.accept()
        except Exception:
            print('---no new client---')
            time.sleep(1)
        else:
            print('---new client---')
            client_socket.setblocking(False)
            client_socket_list.append(client_socket)

        for new_socket in client_socket_list:
            print(client_socket_list)
            try:
                recv_data = new_socket.recv(1024).decode('utf-8')
            except Exception:
                print('---no message---')
                #time.sleep(1)
            else:
                print('---new message---')
                if recv_data:  #如果有数据就调用函数
                    handle_client(new_socket,recv_data)
                else:  #如果没有数据，说明客户端已经挥手，关闭套接字
                    print('*************delete*************')
                    new_socket.close()
                    client_socket_list.remove(new_socket)

                    
    server_socket.close()

if __name__ == "__main__":
    main()
