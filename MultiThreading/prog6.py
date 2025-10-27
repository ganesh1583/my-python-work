import time
from threading import *


def display():
    print("Display thread name : ",current_thread().name)

def show():
    print("No of threads when i am in show : ",active_count())
    print("Show thread name : ",current_thread().name)

print("No of threads in program before creating thread : ",active_count())
t1 = Thread(target=display)
t1.start()

print("No of threads in program after creating 1 thread ",active_count())

t2 = Thread(target=show)
t2.start()


print("No of threads in program in main: ",active_count())
