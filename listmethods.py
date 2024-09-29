# list methods

l = [11, 15, 2, 2, 3, 5, 7, 6]
print(l)
l.append(10)
l.sort()
l.reverse()
print(l.index(2))
print(l.count(3))
m = l.copy()
m[0] = 0
l.insert(1, 45)
m = [100, 200, 300]
l.extend(m)
n = l + m
print(n)