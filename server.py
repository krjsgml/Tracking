# 여러 클라이언트가 접속 가능한 서버 프로그램
import socket, time, threading

def f1(soc): # 클라이언트 소켓(soc)을 parameter로 사용
    while True:
        data = soc.recv(100)
        msg = data.decode() 
        print('recv msg:', msg)
        soc.sendall(msg.encode(encoding='utf-8'))
        if msg == '/end':
            break

def main():
    host = '192.168.0.11'
    port = 3333

    # 서버소켓 오픈
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))

    # 클라이언트 접속 준비 완료
    server_socket.listen()
    print('echo server start')

    # 접속대기 반복(여러 클라이언트)
    while True:
        client_soc, addr = server_socket.accept() # 접속대기
        # 클라이언트 연결 시, 1:1 통신소켓을 오픈 +쓰레드에 전달/실행
        th = threading.Thread(target=f1, args=(client_soc,))  
        th.start()
        print('connected client addr:', addr)
        print('\n client : ', client_soc)


    time.sleep(5)
    print('서버 종료')
    server_socket.close()

main()