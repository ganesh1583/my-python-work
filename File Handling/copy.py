f1 = open(input("Enter name of source file : "),"rb+")
f2 = open(input("Enter file name for copied file : "),"wb+")

data = f1.read()
f2.write(data)

f1.close()
f2.close()