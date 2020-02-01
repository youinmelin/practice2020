# 非堵塞方式单进程线程实现并发方法,并实现长链接
# 修改为面向对象方式
import re
import socket
import time

class HttpServer():
    # 功能：接收客户端发来的请求信息，传递给框架，并接收框架处理好的信息，传递给客户端。
    # 此类提供http服务器功能，仅仅负责接收发送数据，不处理数据。数据处理功能通过传递参数交给框架类处理
    def __init__(self,web_frame):
        self.recv_data_from_client = '' 
        self.recv_data_from_frame = ''
        self.web_frame = web_frame #接收框架对象作为参数传递进来
        print(self.recv_data_from_client)
    
    def run_forever(self):
        #print(recv_data_from_frame)
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
                    self.recv_data_from_client = new_socket.recv(1024).decode('utf-8')
                except Exception:
                    print('---no message---')
                    #time.sleep(1)
                else:
                    print('---new message---')
                    if self.recv_data_from_client:  #如果有数据就调用函数
                        send_data = self.web_frame.handle_client(self.recv_data_from_client)
                        new_socket.send(send_data)
                    else:  #如果没有数据，说明客户端已经挥手，关闭套接字
                        print('*************delete*************')
                        new_socket.close()
                        client_socket_list.remove(new_socket)
        server_socket.close()
    def send_to_frame(self):
        return self.recv_data_from_client

class WebFrame():
    # 功能：接收服务器传来的请求信息，处理后再向服务器传回相应的response信息
#    def __init__(self,recv_data):
#        self.recv_data = recv_data

    def handle_client(self,recv_data):
        print(recv_data)
        recv_data_list = recv_data.splitlines()
        ret = re.match(r"[^/]+(/[^ ]*)", recv_data_list[0])
        if ret:
            file_name = ret.group(1)
            if file_name == '/':
                file_name = '/index.html'
        else:
            file_name = '/index.html'
        print(file_name)
        response_body = self.read_file(file_name)
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
        #print(response.decode('utf-8'))
        return response
    
    def read_file(self,file_name):
        try:
            with open ('./html'+file_name,'rb') as f:
                file_content = f.read()
        except Exception as e:
            file_content = 'error'
            print(e)
        return file_content

def main():
    #recv_data = 'GET /hello.txt HTTP/1.1'
    web_frame = WebFrame()
    http_server = HttpServer(web_frame)
    http_server.run_forever()

if __name__ == "__main__":
    main()
