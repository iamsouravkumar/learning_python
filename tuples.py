tup = (1, 2, 3, 10, 25, 31, 42)
# tup[0] = 100
print(type(tup), tup)
print("Length of tuple is", len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
print(tup[1:4])

if 25 in tup:
    print("Yes")