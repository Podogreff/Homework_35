import socket

HOST = "127.0.0.1"
PORT = 11111

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))


# Cesar function
def encypt_func(txt):
    result = ""

    for i in range(len(txt)):
        char = txt[i]

        if char.isupper():
            result += chr((ord(char) - 61) % 26 + 65)
        else:
            result += chr((ord(char) - 93) % 26 + 97)
    return result


while True:
    data, addr = sock.recvfrom(4096)
    print(data)
    decode_data = data.decode('utf-8')
    cesar_data = encypt_func(decode_data)
    encode_data = cesar_data.encode('utf-8')
    sock.sendto(encode_data, addr)
