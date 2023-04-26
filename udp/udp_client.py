import socket

IP_ADDRESS = '0.0.0.0'

def main():
    server_address = ((IP_ADDRESS, 12345))
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect(server_address)

    while True:
        text = input()
        client.sendto(text.encode(), server_address)
        data = client.recvfrom(4096)
        print(data[0])
    
    client.close()

if __name__ == '__main__' :
    main()