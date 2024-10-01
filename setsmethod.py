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