import socket

host = '127.0.0.1'
port = 3500

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print('SERVER: ' + str(server_socket))

while True:
	connection, address = server_socket.accept()
	
	if(connection):
		while True:
			data = connection.recv(1024)
			full_message += data.decode('utf-8')
			if len(data) == 0:
				break
		print(full_message)
		connection.close()
		

