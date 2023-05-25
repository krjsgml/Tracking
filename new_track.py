import socket
from _thread import *
import numpy as np
import cv2

# Tracking start flag 
# 0이면 stop
# 1이면 start
start_flag = False
TRK_flag = False

# trackerKCF 모델 생성
trackerKCF = cv2.TrackerKCF_create()

# haarcascade
#face_detector = cv2.CascadeClassifier('C:/Users/qhfn7/anaconda3/envs/Yolo_V4/Library/etc/haarcascades/haarcascade_frontalface_default.xml')
face_detector = cv2.CascadeClassifier('C:/Users/qhfn7/anaconda3/envs/Yolo_V4/Library/etc/haarcascades/haarcascade_upperbody.xml')

# socket에서 수신한 버퍼를 반환하는 함수
def recvall(sock, count):
    # 바이트 문자열
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

# 트래킹 클라이언트에게 전송
def TRK_():
    global start_flag
    global TRK_flag
    global trackerKCF
    while start_flag:
        _, frame = cv2.read()
        frame = cv2.flip(frame,1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        # 프레임에 사람이 없으면 no body in cam 출력
        if len(faces) == 0:
            print('no body in cam')
            continue

        else:
            # haarcascade로 받은 튜플 인자들을 저장
            trackObjectTuple = (faces[0,0], faces[0,1], faces[0,2], faces[0,3])

            # 초기값 설정
            result = trackerKCF.init(frame, trackObjectTuple)

            # haarcascade로 부터 인자들을 받고 start tracking
            print("strat tracking the user")
            TRK_flag = True
            break
    
    while start_flag or TRK_flag:
        _, frame = cv2.read()
        frame = cv2.flip(frame,1)
        # haarcascade로 부터 받은 튜플을 이용하여 treackerKCF 업데이트
        # haarcascade로부터 받은 튜플이 프레임에서 변하면 업데이트
        isUpdated, trackObjectTuple = trackerKCF.update(frame)
        if isUpdated:
            x1 = (int(trackObjectTuple[0]) , int(trackObjectTuple[1]) ) 
            x2 = (int(trackObjectTuple[0] + trackObjectTuple[2]), int(trackObjectTuple[1] + trackObjectTuple[3])) 
            cv2.rectangle(frame, x1, x2, (255, 0, 0), 2) 
        
        # 창 띄우기
        cv2.imshow("track object", frame) 
        cv2.waitKey(1)

        #x_frame = str(int(trackObjectTuple[0] + (trackObjectTuple[2]/2)))
        #y_frame = str(int(trackObjectTuple[1] + (trackObjectTuple[3]/2)))

        ## 좌측 상단
        #if int(trackObjectTuple[0] + (trackObjectTuple[2]/2)) < 270 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) < 100:
        #    #print('low left')
        #    msg = "w"
        #    client.send(msg.encode())
#
        ## 좌측 중간
        #elif int(trackObjectTuple[0] + (trackObjectTuple[2]/2)) < 270 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) >= 100 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) <= 190:
        #    #print('mid left')
        #    msg = "s"
        #    client.send(msg.encode())
#
        ## 좌측 하단
        #elif int(trackObjectTuple[0] + (trackObjectTuple[2]/2)) < 270 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) < 480:
        #    #print('high left')
        #    msg = "x"
        #    client.send(msg.encode())
#
        ## 중간 상단
        #elif int(trackObjectTuple[0] + (trackObjectTuple[2]/2)) >= 270 and \
        #    int(trackObjectTuple[0] + (trackObjectTuple[2]/2)) <= 370 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) < 100:
        #    #print('low front')
        #    msg = "e"
        #    client.send(msg.encode())
#
        ## 중간 중간
        #elif int(trackObjectTuple[0] + (trackObjectTuple[2]/2)) >= 270 and \
        #    int(trackObjectTuple[0] + (trackObjectTuple[2]/2)) <= 370 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) >= 100 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) <= 190:
        #    #print('mid front')
        #    msg = "d"
        #    client.send(msg.encode())
#
        ## 중간 하단
        #elif int(trackObjectTuple[0] + (trackObjectTuple[2]/2)) >= 270 and \
        #    int(trackObjectTuple[0] + (trackObjectTuple[2]/2)) <= 370 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) < 480:
        #    #print('high front')
        #    msg = "c"
        #    client.send(msg.encode())
#
        ## 우측 상단
        #elif int(trackObjectTuple[0] + (trackObjectTuple[2]/2)) < 640 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) < 100:
        #    #print('low right')
        #    msg = "r"
        #    client.send(msg.encode())
#
        ## 우측 중단
        #elif int(trackObjectTuple[0] + (trackObjectTuple[2]/2)) < 640 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) >= 100 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) <= 190:
        #    #print('mid right')
        #    msg = "f"
        #    client.send(msg.encode())
#
        ## 우측 하단
        #elif int(trackObjectTuple[0] + (trackObjectTuple[2]/2)) < 640 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) < 480:
        #    #print('high right')
        #    msg = "v"
        #    client.send(msg.encode())
#
        ## 매우 가까운 경우
        #elif int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) <= 50 and \
        #    int(trackObjectTuple[1] + (trackObjectTuple[3]/2)) >= 0:
        #    #print("User very close")
        #    msg = "q"
        #    client.send(msg.encode())

    cv2.destroyAllWindows()
    trackerKCF = cv2.TrackerKCF_create()
    TRK_flag = False
    print('init TRK info')


# 트래킹 전 카메라로 테스트 진행
# client_TRK로부터 프레임 데이터를 받으면 decode 이후,
# cv imshow() 진행
def CAM_TEST(client1):
    global start_flag
    while start_flag:
        length = recvall(client1, 16)
        stringData = recvall(client1, int(length))
        data = np.fromstring(stringData, dtype='uint8')
        frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
        cv2.imshow("track object", frame)
        cv2.waitKey(1)

    cv2.destroyAllWindows()

# 트래킹을 하면서 같이 client_gui에서 데이터를 받아와야하므로
# 새로운 쓰레드를 생성하여 통신
# 0을 받으면 start_flag = 0 / 1을 받으면 start_flag = 1이 됨
def thread_recv_gui(client_socket, addr):
    global start_flag
    global TRK_flag

    while True:
        try:
            # clinet_GUI로 부터 데이터를 받아옴
            data = client_socket.recv(1024)

            # data가 1이면 stop_flag가 1이 됨
            if data.decode() == '1':
                start_flag = True
                TRK_flag = True

                # data를 client_TRK로 보냄
                if data == '':
                    continue

                else:
                    client_socket.send(data)
            
            # data가 0이면 stop_flag가 0이 됨
            elif data.decode() == '0':
                client_socket.send(data)
                start_flag = False
                TRK_flag = False

        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

        if client_socket in client_sockets:
            client_sockets.remove(client_socket)
            print('remove client list : ',len(client_sockets))

    client_socket.close()

# 쓰레드에서 실행되는 코드입니다.
# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다.
def threaded(client_socket, addr):
    # 클라이언트가 접속을 끊을 때 까지 반복합니다.
    while True:
        try:
            # 카메라 테스트
            #CAM_TEST(client_TRK)
            # 클라이언트로 treakerKCF에 대한 프레임 영역을 클라이언트로 보냄
            TRK_()
           
        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

    if client_socket in client_sockets :
        client_sockets.remove(client_socket)
        print('remove client list : ',len(client_sockets))

    client_socket.close()

# flag를 정하는 쓰레드 생성
# client_GUI에서 받은 신호로 flag 생성

client_sockets = [] # 서버에 접속한 클라이언트 목록

# tcp/ip init
server_ip = '192.168.0.11' # 위에서 설정한 서버 ip
server_ip = '10.254.3.11'
server_port = 3333 # 위에서 설정한 서버 포트번호

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# server connect
print('client on')
try:
    while True:
        print('>> Wait')
        # thread 시작
        start_new_thread(threaded, (client_socket, addr))
        start_new_thread(thread_recv_gui, (client_socket, addr))

except Exception as e :
    print ('에러는? : ',e)

finally:
    # 서버 프로그램 종료시 socket close
    client_socket.close()

# 창 모두 닫기
cv2.destroyAllWindows()