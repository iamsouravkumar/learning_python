# recursive function

def factorial(n):
    if(n==0 or n==1):
        return 1
    
    else:
        return n * factorial(n-1)
    
num = int(input("Enter a Number: "))
print(f"The Factorial of {num} is " + str(factorial(num)))

# fibbonacci series

def fseries(i):
    if i <= 1:
        return 1
    else:
        return(fseries(i-1) + fseries(i-2))

num = int(input("Number upto print fibbonaci series: "))
if(num <=0 ):
    print("Please enter a positive number")

else:
    print(f"Fibbonaci series upto number {num} is:")
    for i in range(num):
        print(fseries(i))