# 非堵塞方式单进程线程实现并发方法
import socket
import time

def handle_client(client_socket,recv_data):
#    recv_data = client_socket.recv(1024).decode('utf-8')
    print(recv_data)
    recv_data_list = recv_data.split()
    print(recv_data_list[1])
    response_header = 'HTTP/1.1 200 OK\r\n'
    response_header += '\r\n'
    # file_name
    response_body = recv_data_list[1]
    response = response_header + response_body
    response = response_header
    client_socket.send(response.encode('utf-8'))
    file_data = read_file(recv_data_list[1])

    client_socket.send(file_data)
    client_socket.close()
    return 0

def read_file(file_name):
    try:
        with open (file_name[1:],'rb') as f:
            file_content = f.read()
    except Exception:
        file_content = b'<h1>404 error</h1>'
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
                if recv_data:
                    handle_client(new_socket,recv_data)
                    client_socket_list.remove(new_socket)
                    print('*************delete*************')
                else:
                    print('-------no message-----')

                    
    server_socket.close()

if __name__ == "__main__":
    main()
