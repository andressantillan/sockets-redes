import socket

IP_ADDRESS =  '0.0.0.0'

print(f'====== Starting service in  {IP_ADDRESS}:12345 ======')
server_address = ((IP_ADDRESS, 12345))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_address)
server.listen()

connection, client_address = server.accept()
msg = b'Ingrese un numero:'
nums = []

try:
    while True:
        while len(nums) < 2:
            connection.send(msg)
            data = connection.recv(4096)
            try:
                nums.append(int(data.decode()))
            except ValueError:
                aux = f'{data.decode()} is not an integer.\n'
                connection.send(aux.encode())
                nums.clear()
        
        resultado = nums[0] + nums[1]
        aux = (str(resultado) + '\n').encode()
        nums.clear()
        connection.send(aux)
except: 
    print('received data is no printable')
        
connection.close()
print('====== Service down ======')	