from os import popen
from threading import Thread as th
from time import sleep




def for_loop(number,sign):
    for i in range(0,number):
        print(sign+str(i))
        sleep(0.5)

def test(test):
    print(test)

# _thread.start_new_thread ( function, args[, kwargs] )
# for thread function not whit argoman
t1 = th(target=for_loop, args=(500, " *** "))
t2 = th(target=for_loop, args=(500, " ---"))
t3 = th(target=for_loop, args=(500, "222"))
t4 = th(target=test, args=("reza", ))





t4.start()
t1.start()
t2.start()
t3.start()
