import socket

IP_ADDRESS = '0.0.0.0'

def main():
    server_address = ((IP_ADDRESS, 12345))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server_address)

    while True:
        data = client.recv(4096)
        print(data.decode())
        text = input()
        client.send(text.encode())
    
    client.close()

if __name__ == '__main__' :
    main()