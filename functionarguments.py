# default arguments

def average(a=5, b=5):
    print("The average is ", (a+b)/2)

average(b=6)

# keyword arguments

def name(fname, mname = "john", lname = "watson"):
    print("hello", fname, mname, lname)

name("Amy", "Aggarwal", "John")

# variable length arguments

def average(*numbers):
    sum= 0
    for i in numbers:
        sum = sum + i
    # print("The average is ", sum / len(numbers))
    return sum / len(numbers)

c = average(4, 8, 2, 6)
print(c)

# keyword arbitrary arguments

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan,", lname = "Barnes", fname = "James,")