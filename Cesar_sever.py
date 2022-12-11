import socket

HOST = "127.0.0.1"
PORT = 11111


# Cesar function
def encrypt_func(txt):
    result = ""
    for i in range(len(txt)):
        char = txt[i]
        if char.isupper():
            result += chr((ord(char) - 61) % 26 + 65)
        else:
            result += chr((ord(char) - 93) % 26 + 97)
    return result


def udp_server(host=HOST, port=PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    try:
        data, addr = sock.recvfrom(4096)
        if data:
            print(data)
            decode_data = data.decode('utf-8')
            cesar_data = encrypt_func(decode_data)
            sock.sendto((bytes(cesar_data, encoding='utf-8')), addr)
    except socket.error:
        print(f'Sorry, {socket.error}')
    finally:
        sock.close()


if __name__ == '__main__':
    udp_server()
