import socket

HOST = "127.0.0.1"
PORT = 11111

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Hello from CLIENT"
client_socket.sendto(msg.encode('utf-8'), (HOST, PORT))
data, addr = client_socket.recvfrom(4096)
print('Server says:')
print(str(data))
client_socket.close()
