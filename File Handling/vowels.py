f = open("t.txt","r")

v = ['a','e','i','o','u','A','E','I','O','U']

cnt = 0
i = 0
while True:
	ch = f.read(1)
	if ch == "":
		print("\nEnd is reached")
		break
	else:
		
		if ch in v:
			print(i,end=" ")
			cnt+=1
		i += 1

print("No of vowels : ",cnt)

print()
f.close()