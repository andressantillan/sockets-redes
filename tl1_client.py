import socket

def main():
    server_address = (('0.0.0.0', 12345))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server_address)
    client.send('Client'.encode())
    resp_server = client.recv(4096)
    client.close()
    print(resp_server.decode())

if __name__ == '__main__' :
    main()