# set methods
# union

s1 = {1,2,5,6}
s2 = {3,6,7}

print(s1.union(s2))
print(s1, s2)
s1.update(s2)
print(s1, s2)

cities = {"Delhi", "Mumbai", "Chennai", "Tokyo"}
cities2 = {"London", "Paris", "Chennai", "Tokyo"}
cities3 = cities.union(cities2)
print(cities3)

# intersection

cities = {"Delhi", "Mumbai", "Chennai", "Tokyo"}
cities2 = {"London", "Paris", "Chennai", "Tokyo"}
cities3= cities.intersection(cities2)
cities.intersection_update(cities2)
print(cities3)
print(cities)

# symmetric difference

cities = {"Delhi", "Mumbai", "Chennai", "Tokyo"}
cities2 = {"London", "Paris", "Chennai", "Tokyo"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# difference and difference update

cities = {"Delhi", "Mumbai", "Madrid", "Kabul"}
cities2 = {"London", "Paris", "Madrid", "Kabul"}
cities3 = cities.difference(cities2)
print(cities3)

# manipulation of sets

# isdisjoint

cities = {"Delhi", "Mumbai", "Chennai2", "Tokyo2"}
cities2 = {"London", "Paris", "Chennai", "Tokyo"}
cities3 = cities.isdisjoint(cities2)
print(cities3)

# issuperset

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Tokyo", "Madrid", "Delhi"}
print(cities.issuperset(cities3))

# issubset

print(cities3.issubset(cities))

# add

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Kabul")
print(cities)

# update

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Ghaziabad"}
cities.update(cities2)
print(cities)

# remove / discard

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Delhi2")
cities.discard("Delhi2")
print(cities)

# pop

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(item)
print(cities)

# del / clear

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
cities.clear()
print(cities)

info = {"Sourav", 19, 5.3, 19, True}

if "Sourav" in info:
    print("Sourav is present")
else:
    print("Sourav is not present")