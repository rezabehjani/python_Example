#! /usr/bin/env python3
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def main():
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(target=test, args=(synchronizer, serializer)).start()
    Process(target=test, args=(synchronizer, serializer)).start()

def test(synchronizer, serializer):
    synchronizer.wait()
    now = time()
    with serializer:
        print(datetime.fromtimestamp(now))

if __name__ == '__main__':
    main()