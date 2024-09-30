# doc strings are write just after the start of the function or write in the function body

def square(n):
    # print(n)
    '''Takes in a number n, returns the square of n'''
    print(n**2)

square(5)

#it will print the doc string
print(square.__doc__)