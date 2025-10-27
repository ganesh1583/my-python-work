import time
from threading import Thread

def display():
    for i in range(1,6):
        print(i,": display thread")
        time.sleep(1)

def show():
    for i in range(1,6):
        print(i,": show thread")
        time.sleep(1)

t1 = Thread(target=display)
t1.start()

t2 = Thread(target=show)
t2.start()

for i in range(1,6):
    print(i,": Main Thread")
    time.sleep(1)
