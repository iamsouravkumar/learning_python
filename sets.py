# sets does not repeat the elements
# sets are unordered
# sets are mutable
# sets are iterable
# sets are not subscriptable

s = {2, 4, 2, 6}
print(s)

info = {"Sourav", 19, 5.3, 19, True}
print(info)

sourav = {} # empty dictionary not an empty set
sourav2 = set() # use set() to create an empty set
print(type(sourav))
print(type(sourav2))

for value in info:
    print(value)