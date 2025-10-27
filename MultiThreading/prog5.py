import time
from threading import *

def display():
    print("Information of display thread : ")
    myname = current_thread().name
    myid = current_thread().ident
    print("Thread name : ",myname)
    print("Thread id : ",myid)

t = Thread(target=display,name="mythread")
t.start()

time.sleep(1)

print("Information of main thread : ")
myname = current_thread().name
myid = current_thread().ident
print("Thread name : ",myname)
print("Thread id : ",myid)
