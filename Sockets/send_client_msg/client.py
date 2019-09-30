import socket

host = '127.0.0.1'
port = 3500

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

print('CLIENT: ' + str(client_socket))

client_socket.send(b'Hello Server!')
client_socket.close()