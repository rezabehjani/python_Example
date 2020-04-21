import socket
import threading

disconnect = False

def recieve(client):
    global  disconnect
    while True:
        try:
            message = client.recv(1024)
            if message == b'':
                print("client disconnected")
                disconnect = True
                break
            else:
                print((message.decode()))
        except Exception as e:
            print("client disconnected")
            disconnect = True
            break

def send(client):
    global  disconnect
    while True:
        message = input()
        if not disconnect:
            client.send(message.encode(()))
        else:
            break


host = '94.183.231.63' # The remote host
port = 6500  # The same port as used by the server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))

server.listen()
print("serving on {}".format(server.getsockname()))
while True:
    client, addr = server.accept()
    client.settimeout(100)
    print("new connection {}".format(addr))
    t1 = threading.Thread(target=recieve, args=(client,))
    t1.daemon = True
    t1.start()
    t1 = threading.Thread(target=send, args=(client,))
    t1.daemon = True
    t1.start()

