import socket
import string
import random
import time

IP_ADDRESS = '127.0.0.1'

def suma(connection):
	data = connection.recv(4096)
	args = data.decode().split(' ')
	msg = ''

	if len(args) < 2:
		connection.send('Faltan argumentos.'.encode())
		return False

	if len(args) > 2:
		connection.send('Solo 2 enteros.'.encode())
		return False
	
	for x in args:
		try:
			int(x)
		except ValueError:
			msg += f'{x} no es un entero. '
	
	if msg != '':
		connection.send(msg.encode())
		return False

	resultado = int(args[0]) + int(args[1])
	connection.sendall(str(resultado).encode())

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
	print(f'====== Starting service in  {IP_ADDRESS}:12345 ======')
	server_address = ((IP_ADDRESS, 12345))

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server.bind(server_address)
	server.listen()

	connection, client_address = server.accept()
	
	try:
		while True:
			suma(connection)
	except:
		print('recieved data is no printable')

	connection.close()
	print('====== Service down ======')	

if __name__ == '__main__':
	main()