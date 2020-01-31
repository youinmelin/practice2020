# http 服务器，加入多线程方式
import socket
import threading 

def handle_client(client_socket):
    recv_data = client_socket.recv(1024).decode('utf-8')
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
    print(response)

    file_data = read_file(recv_data_list[1])
    client_socket.send(file_data)
    client_socket.close()

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
    while True:
        client_socket,client_addr = server_socket.accept()
        p = threading.Thread(target = handle_client, args=(client_socket,))
        p.start()
        #client_socket.close() 子线程不复制主线程的资源，所以不用关闭两次

    server_socket.close()

if __name__ == "__main__":
    main()
