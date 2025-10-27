
f = open("a.txt","a")
print(f)
print(type(f))
print(id(f))

print("File name : ",f.name)
print("File mode : ",f.mode)
print("Is readable : ",f.readable())
print("Is writable : ",f.writable())
print("Is closed : ",f.closed)

f.close()

print("Is clodes now : ",f.closed)