import sys
import socket
import traceback
import time

def do_work():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # timeout recv every 5 seconds
    sock.settimeout(5.0) 

    # check and turn on TCP Keepalive
    x = sock.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE)
    if (x == 0):
        print('Socket Keepalive off, turning on')
        x = sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        print(str(x))
        # overrides value (in seconds) shown by sysctl net.ipv4.tcp_keepalive_time
        sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 60)
        # overrides value shown by sysctl net.ipv4.tcp_keepalive_probes
        sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, 4)
        # overrides value shown by sysctl net.ipv4.tcp_keepalive_intvl
        sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 15)
    else:
        print('Socket Keepalive already on')

    try:
        sock.connect(('192.168.0.120', 8001))

    except socket.error:
        print('Socket connect failed!')
        traceback.print_exc()
        return

    print('Socket connect worked!')
    while True:
        try:
            # read at most 10 bytes (or less)
            req = sock.recv(10)

        except socket.timeout:
            print('Socket timeout, loop and try recv() again')
            continue

        except:
            traceback.print_exc()
            print('Other Socket err, exit and try creating socket again')
            # break from loop
            break

        if req == '':
            # connection closed by peer, exit loop
            print('Connection closed by peer')
            break

        print('Received', req)

    try:
        sock.close()
    except:
        pass   


if __name__ == '__main__':
    do_work()

# references
# http://tldp.org/HOWTO/html_single/TCP-Keepalive-HOWTO/
# http://www.digi.com/wiki/developer/index.php/Handling_Socket_Error_and_Keepalive