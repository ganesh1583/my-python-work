n = int(input("Enter number : "))

if n < 0:
	print("Negative number cannot be prime")
else:
	for i in range(2,n//2):
		if n % i == 0:
			print(n,"is not a prime number")
			break
	else:
		print(n,"is a prime number")