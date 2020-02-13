# Echo client program
import socket
import time
from datetime import datetime
import threading
HOST = '94.183.231.63'    # The remote host
#HOST = '192.168.10.250'    # The remote host
PORT = 6500              # The same port as used by the server

def connection_check():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

                s.connect((HOST, PORT))
                for x in range(0, 55):
                        s1 = datetime.now()
                        s.sendall(b'>>N,522274280,23,522274280;')
                        # data = s.recv(1024)
                        # print('Received', repr(data))
                        # time.sleep(11)
                        # s.close()



                #time
                s2 = datetime.now()
                elapsedTime = s2 - s1
                print(divmod(elapsedTime.total_seconds(), 60))
timer1 = threading.Timer(3.0, connection_check)
timer1.start()
# timer2 = threading.Timer(3.0, connection_check)
# timer2.start()
# timer3 = threading.Timer(3.0, connection_check)
# timer3.start()
# timer4 = threading.Timer(3.0, connection_check)
# timer4.start()
# timer5 = threading.Timer(3.0, connection_check)
# timer5.start()
