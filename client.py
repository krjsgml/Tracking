# 클라이언트
import socket

server_ip = '192.168.0.11' # 위에서 설정한 서버 ip
server_port = 3333 # 위에서 설정한 서버 포트번호

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((server_ip, server_port))

# /end 입력될 때 까지 계속해서 서버에 패킷을 보냄
while True:
    msg = input('msg:') 
    socket.sendall(msg.encode(encoding='utf-8'))
    data = socket.recv(100)
    msg = data.decode() 
    print('echo msg:', msg)
    
    if msg == '/end':
        break

socket.close()