import time
from threading import *

def display():
    print("Display thread name : ",current_thread().name)


t1 = Thread(target=display)
t2 = Thread(target=display)
t3 = Thread(target=display)

t1.start()
t2.start()
t3.start()
print("No of active threads : ",active_count())

print("List of active threads : ")
thread = enumerate()

for i in thread:
    print("Thread name ",i.name)

time.sleep(5)


print("List of active threads : ")
thread = enumerate()

for i in thread:
    print("Thread name ",i.name)

