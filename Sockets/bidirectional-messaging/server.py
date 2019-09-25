import socket

host = '127.0.0.1'
port = 3500

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

while True:
	connection, address = server_socket.accept()
	
	while(connection):
		#receive message
		while True:
				data = client_socket.recv(1024)
				if len(data) == 0:
					break
				print(data.decode('utf-8')
	
		#send message
		server_message = input('> ')
		connection.send(bytes(server_message, 'utf-8'))
		print('SERVER: ' + server_message)
	connection.close()