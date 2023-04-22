import socket
import string
import random
import time

def recv_message(connection):
	data = connection.recv(4096)
	print(data.decode())

def echo(connection):
	data = connection.recv(4096)
	connection.sendall(data)

def character_generator(connection):
	letters = string.ascii_lowercase
	msg = ''.join(random.choice(letters))
	connection.send(msg.encode())
	time.sleep(1)

def main():
	print('====== Starting service in  0.0.0.0:12345 ======')
	server_address = (('0.0.0.0', 12345))

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server.bind(server_address)
	server.listen()

	connection, client_address = server.accept()
	
	try:
		while True:
			recv_message(connection)
	except:
		print('received data is not printable')

	connection.close()
	print('====== Service down ======')	

if __name__ == '__main__':
	main()