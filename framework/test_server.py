from socket import socket, AF_INET, SOCK_STREAM


SERV_SOCK = socket(AF_INET, SOCK_STREAM)
SERV_SOCK.bind(('127.0.0.1', 8001))
SERV_SOCK.listen(1)

while True:
    CLIENT_SOCK, ADDR = SERV_SOCK.accept()
    print(f'Получен запрос на соединение от клиента с адресом и портом: {ADDR}')
    DATA = CLIENT_SOCK.recv(1024).decode('utf-8')
    print(DATA)
    CLIENT_SOCK.close()
    
SERV_SOCK.close()