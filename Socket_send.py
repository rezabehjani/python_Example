# Echo client program
import socket
import time
from datetime import datetime
import threading
HOST = '94.183.231.63'    # The remote host
#HOST = '192.168.10.250'    # The remote host
PORT = 6500              # The same port as used by the server
ddd = 1
def connection_check():
        dd = 1
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                while True:
                        print(dd)
                        dd += 1

                        s.sendall(b'{"Info":{"Command":5,"Action":"Get","Type":1,"Data":{"user":"reza","pass":"1234"}},"Time":"Wed Apr 01 23:07:13 GMT+04:30 2020","To":{"Type":"S","Token":"2222","Rule":2},"From":{"Type":"P","Token":"123","Rule":1}}\n')
                        data = s.recv(1024)
                        # if len(data) >= 600:
                        #         print('Received', repr(data))
                        # time.sleep(11)
                        # s.close()

while True:
        print(ddd)
        ddd += 1
        timer1 = threading.Timer(1.0, connection_check)
        timer1.start()
# timer2 = threading.Timer(3.0, connection_check)
# timer2.start()
# timer3 = threading.Timer(3.0, connection_check)
# timer3.start()
# timer4 = threading.Timer(3.0, connection_check)
# timer4.start()
# timer5 = threading.Timer(3.0, connection_check)
# timer5.start()
