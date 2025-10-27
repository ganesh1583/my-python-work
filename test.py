i = 3
j = id(3)
print(globals())
del i
print(globals())
i = None
id(i) = j
print(i)
