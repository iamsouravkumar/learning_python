# operations in tuples

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

# concatenate two tuples without convertng them to lists

countries = ("Pakistan", "Afghanistan", "Bangladesh", "Sri Lanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
# res = tuple1.index(311)
# res = tuple1.index(3, 4, 8)
res = len(tuple1)
print("Count of 3 in tuple1 is:", res)