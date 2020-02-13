import socket
import sys
def main():
   soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host = "95.216.122.4"
   port = 2323
   try:
      soc.connect((host, port))
   except:
      print("Connection Error")
      sys.exit()
   print("Please enter 'quit' to exit")
   message = input(" -> ")
   while message != 'quit':
      soc.sendall(message.encode("utf8"))
      if soc.recv(5120).decode("ASCII") == "-":
         pass # null operation
      message = input(" -> ")
   soc.send(b'--quit--')
if __name__ == "__main__":
   main()