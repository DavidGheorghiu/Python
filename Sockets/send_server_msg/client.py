import socket

host = '127.0.0.1'
port = 3500

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
	data = client_socket.recv(1024)
	if len(data) == 0:
		break
	print(data.decode('utf-8'))