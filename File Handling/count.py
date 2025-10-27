f = open("t.txt","r")

wc = 0
cc = 0
lc = 0

for i in f:
	lc+=1
	cc+=len(i)
	L = i.split()
	wc+=len(L)

print("Word count : ",wc)
print("Character count : ",cc)
print("Line count : ",lc)


f.close()