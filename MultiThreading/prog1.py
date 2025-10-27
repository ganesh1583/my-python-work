import time

def display():
	for i in range(1,6):
		print(i,": Display Thread")
		time.sleep(1)


def show():
	for i in range(1,6):
		print(i,": Show Thread")
		time.sleep(1)


display()
show()

for i in range(1,6):
	print(i,": Main Thread")
	time.sleep(1)
	