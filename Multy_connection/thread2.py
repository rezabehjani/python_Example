import socket, threading


class ClientThread(threading.Thread):


    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)

    def run(self):
        print ("Connection from : ", clientAddress)



        while True:
            try:

                data = self.csocket.recv(2048)
                print ("from client", repr(data))
                self.csocket.sendall(b'reza')
            except IOError as error:
                print(error)
                self.csocket.close()
                self._stop()
                print ("Client at ", clientAddress , " disconnected...")





LOCALHOST = '192.168.1.249'
PORT = 2323
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(5)

    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()