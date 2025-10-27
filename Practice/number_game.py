from random import randint

while True:
	try:
		print("Choose Difficulty Level :")
		print("1.Easy \n2.Mediun \n3.Diffucult\n")
		dl = int(input("Enter here : "))
	except Exception:
		print("Try Again!!!\n")
	else:
		break

if dl == 1:
	act_num = randint(1,10)
elif dl==2:
	act_num = randint(1,20)
elif dl==3:
	act_num = randint(1,100)
else:
	act_num = randint(1,10)
	print("Difficulty Seted To Easy By Default")

while True:
	while True:
		try:
			g_num = int(input("Enter your guess : "))
		except Exception:
			print("Try Again!!!")
		else:
			break

	if g_num < act_num:
		print("Your guess number is small!!!")
	elif g_num > act_num:
		print("Your guess number is big!!!")
	elif g_num == act_num:
		print("Correct Guess!!!")
		break