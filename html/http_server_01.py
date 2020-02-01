import socket

def handle_client(client_socket):
    recv_data = client_socket.recv(1024).decode('utf-8')
    print(recv_data)
    recv_data_list = recv_data.split()
    print(recv_data_list[1])
    response_header = 'HTTP/1.1 200 OK\r\n'
    response_header += '\r\n'
    response_body = '<h1>hello Nasa</h1>'
    response_body += recv_data_list[1]
    response = response_header + response_body

    file_data = read_file(recv_data_list[1])

    client_socket.send(file_data.encode('utf-8'))
    client_socket.close()

def read_file(file_name):
    with open (file_name[1:]) as f:
        file_content = f.read()
    return file_content

def main():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('',7890))
    server_socket.listen(128)
    while True:
        client_socket,client_addr = server_socket.accept()
        handle_client(client_socket)
    server_socket.close()

if __name__ == "__main__":
    main()
