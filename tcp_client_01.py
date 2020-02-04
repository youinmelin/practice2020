
from socket import *

tcp_client_socket = socket(AF_INET,SOCK_STREAM)

server_ip=input('input server IP:')
server_port = int( input ('input server port:'))

tcp_client_socket.connect((server_ip,server_port))

send_data = input (' input send data : ')
tcp_client_socket.send(send_data.encode('utf-8'))

recvData = tcp_client_socket.recv(1024)
print(f'received data is:{recvData.decode("utf-8")}')
