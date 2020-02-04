from socket import *

tcp_server_socket = socket(AF_INET,SOCK_STREAM)

address = ('',7788)

tcp_server_socket.bind(address)

tcp_server_socket.listen(128)

client_socket,clientAdrr = tcp_server_socket.accept()

recv_data = client_socket.recv(1024)
print(f'received message is : {recv_data.decode("utf-8")}')

client_socket.send('all right'.encode('utf-8'))

client_socket.close()
