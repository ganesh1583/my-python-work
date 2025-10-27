import time
from threading import Thread

class UserThread(Thread):
    def run(self):
        for i in range(1,6):
            print(i,": User thread")
            time.sleep(1)


T = UserThread()
T.start()

for i in range(1,6):
    print("I am in Main Thread ")
    time.sleep(2)

