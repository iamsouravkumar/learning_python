# functions

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a, b):
    pass       

a = 8
b = 9
isGreater(a,b)
calculateGmean(a, b)

a = 10
b = 7
isGreater(a,b)
calculateGmean(a, b)