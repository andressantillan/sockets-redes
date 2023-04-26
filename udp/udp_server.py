import socket

IP_ADDRESS = '0.0.0.0'

def main():
    print(f'====== Starting service in  {IP_ADDRESS}:12345 ======')
    server_address = ((IP_ADDRESS, 12345))

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server.bind(server_address)

    try:
        while True:
            data = server.recvfrom(4096)
            server.sendto(data[0], data[1])
    except:
        print('recieved data is no printable')

    connection.close()
    print('====== Service down ======')	


if __name__ == '__main__':
    main()