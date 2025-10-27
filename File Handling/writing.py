
f = open("a.txt","r+")

data = f.read()
print(data)
f.write("\n")
f.write(input("Enter what you want to write in file : "))
f.write("\n")
data = f.read()
print(data)

s1 = input("Enter first string : ")
s1 = s1 + "\n"
s2 = input("Enter second string : ")
s2 = s2 + "\n"
s3 = input("Enter third string : ")

f.writelines([s1,s2,s3])
f.close()

fp = open("a.txt","r")
data = fp.read()
print(data)

fp.close()
