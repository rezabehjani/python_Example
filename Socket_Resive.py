# Echo server program
import socket
import time
HOST = '192.168.12.253'                 # Symbolic name meaning all available interfaces
PORT = 5665           # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    #for i in range(1, 1000):
    s.listen(2)
    conn, addr = s.accept()
    localtime = time.asctime(time.localtime(time.time()))
    print("Local current time :", localtime)
    with conn:
        print('Connected by', addr)
        s = 0
        while True:
            s += 1
            data = conn.recv(2048)
            print(repr(data))
            if s == 1000:
                s = 0
                print("ok")
                localtime = time.asctime(time.localtime(time.time()))
                print("Local current time :", localtime)
            # if not data: break
            # conn.sendall(b'dfvbvcvbcvbcvbcvmklfgmkljkjmopfgjopnsdtmnpiuvasjadvmouphvnm9fjdropumsdiopghsdbjsgiuejvm,asjmnv,sdjbhmgbumnv[gdovujm,')