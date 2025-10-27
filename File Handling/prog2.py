import _io
f = open("a.txt","a")

#f.write("I am writing this in a.txt\nStraight through my prog2.py\n")
 
s1 = "This is third line\n"
s2 = "Its fourth line for a.txt\n"
s3 = "Bye bye\t\n"

L = [s1,s2,s3]
f.writelines(L)


#help(_io.TextIOWrapper)
f.close()
