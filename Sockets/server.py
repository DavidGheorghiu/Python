import socket

host = '127.0.0.1'
port = 3500

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

while True:
	connection, address = server_socket.accept()
	
	if(connection):
		connection.send(b'hello!')
		connection.close()