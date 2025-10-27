f = open("t.txt","r+")

"""
print("read : ")
data = f.read()
f.seek(0)
print(f.read())
print("\n",data)
"""

#print("\n\n\n\n\n")

"""
print("Readline : ")
data = f.readline()
print(data)

data = f.readline()
print(data)

data = f.readline()
print(data)
data = f.readline()
print(data)

"""

"""
print("Readlines : ")
L = f.readlines(-2)
print(L)
"""

print("read(n) : ")
data = f.read(14)

print(data)


f.close()