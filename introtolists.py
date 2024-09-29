# lists in python

marks= [5, 4, 8, "Sourav", True, 10, 7, 6, 12, 15, 13]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])

if "Sourav" in marks:
    print("Yes")

else:
    print("No")

if "Sou" in "Sourav":
    print("Yes")

print(marks)
print(marks[:])
print(marks[1:9])
print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2 == 0]
print(lst)
