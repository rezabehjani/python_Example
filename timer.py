# Program to demonstrate
# timer objects in python

import threading
import time

def gfg():
    while True:
        time.sleep(3)
        print("GeeksforGeeks\n")


timer = threading.Timer(20, gfg)
timer.start()
print("Exit\n")


while True:
    print("reza")