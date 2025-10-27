import time
from threading import *

def display():
    globals t2
    t2.join()
    for i in range(1,6):
        print(i,": display thread")
        time.sleep(1)


def show():
    for i in range(1,6):
        print(i,": show thread")
        time.sleep(1)


t1 = Thread(target=display)
t1.start()

t1.join()

t2 = Thread(target=show)
t2.start()


for i in range(1,6):
    print(i,": Main thread")
    time.sleep(1)

