import socket

HOST = "127.0.0.1"
PORT = 11111


def udp_message(host=HOST, port=PORT):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input("Please enter the message you want to encrypt: ")
    client_socket.sendto(message.encode('utf-8'), (host, port))
    data, addr = client_socket.recvfrom(4096)

    print(f'Encrypted message from the server: {data.decode("utf-8")}')
    client_socket.close()

    return client_socket


if __name__ == '__main__':
    udp_message()
