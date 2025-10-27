import os

f = open("a.txt","w")

print(os.path.basename(f.name))
print(os.path.abspath(f.name))
print(os.path.realpath(f.name))
print("Parent Directory : ",os.path.dirname(os.path.abspath(f.name)))
