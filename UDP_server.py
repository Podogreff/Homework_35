import socket

HOST = "127.0.0.1"
PORT = 11111

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    data, addr = sock.recvfrom(4096)
    print(str(data))
    message = b"Hello from UDP server"
    sock.sendto(message, addr)
