
import socket
import json

UDP_IP = "192.168.10.250"

UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

sock.bind((UDP_IP, UDP_PORT))

while True:

    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes

    print("received message:", data)

    sock.sendto(data, ("192.168.10.250", 5005))
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)
w = json.dumps(x)

sock.sendto(w.encode("ASCII"), ("192.168.10.250", 5005))
