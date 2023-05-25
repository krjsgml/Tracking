import socket
from _thread import *

HOST = '192.168.0.11'
PORT = 3333

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    data = client_socket.recv(1024)
    sig = data.decode()
    print('recieve :', sig)
    if sig == 'w':
        print("left top")

    elif sig == 'e':
        print("center top")
    
    elif sig == 'r':
        print("right top")
    
    elif sig == 's':
        print("left middle")

    elif sig == 'd':
        print("center middle")

    elif sig == 'f':
        print("right middle")

    elif sig == 'x':
        print("left bottom")

    elif sig == 'c':
        print("center bottom")

    elif sig == 'v':
        print("right bottom")

    elif sig == 'q':
        print('stop')