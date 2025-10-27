import time
from threading import Thread

def addition(a,b):
    for i in range(1,6):
        print("Addition : ",a+b)
        time.sleep(2)

def substraction(a,b):
    for i in range(1,6):
        print("Substraction : ",a-b)
        time.sleep(2)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

T1 = Thread(target=addition,args=([a,b]))
T1.start()

T2 = Thread(target=substraction,args=([a,b]))
T2.start()

for i in range(1,6):
    print("I am in Main Thread ")
    time.sleep(2)

