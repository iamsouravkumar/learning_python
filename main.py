"""
import hashlib #built in module
import pandas #external module
# print('hello world')
# print(10)
# print('sourav')
# print(10*10)

# single line comment
print("hey i am \"sourav\" kumar \ni am a \"coder\"") # \n = escape sequence character

# multi line comment
'''
hey i am "sourav" kumar 
i am a "coder"
'''

# using separaters, separaters are used to seperate the values

print("sourav", 19, 2024, sep="-", end="0000\n")
print("kumar")
"""

# variables and data types

"""
a= 10 # integer
b= "sourav" # string
c= True # boolean
d = None # none
e = complex(10, 20) # complex number
f = 1.5 # float
print(a, b, c, d, e, f)
print(type(a), type(b), type(c), type(d), type(e), type(f))
"""

# operators in puthon

"""
print(5+6) # addition
print(15+6) # addition
print(15-6) # subtraction
print(15*6) # multiplication
print(15/6) # division
print(15%6) # modulus
print(15//6) # floor division
print(5**3) # exponential
"""

# performing calculations using input function 
"""
a = input("enter first number: ")
b = input("enter second number: ")

print("the value of", a, "+", b, "is", int(a) + int(b))
print("the value of", a, "-", b, "is", int(a) - int(b))
print("the value of", a, "*", b, "is", int(a) * int(b))
print("the value of", a, "/", b, "is", int(a) / int(b))
print("the value of", a, "//", b, "is", int(a) // int(b))
print("the value of", a, "%", b, "is", int(a) % int(b))
print("the value of", a, "**", b, "is", int(a) ** int(b))
"""

# typecsting or type conversion = typecasting is the process of converting one data type to another data type

"""
a = "1" # string
b= "2" # string
print(int(a)+int(b)) # typecasting or type conversion

# implicit typecasting = automatic typecasting

c = 10
d=1.5
print(c+d)
"""

#strings 

'''str= """hey i am "sourav"
        i am 19 year old
        i am a college student"""
print(str)

for character in str:
    print(character)'''

"""fruit = 'mango'
print(fruit[0:4])
print(len(fruit))
print(fruit[-3:-1])
print(fruit[-4:-2])"""

# string methods in python
#strings are immutable in python

'''a = "!!!Sourav!!! !!!!!! Kumar!!!!"
print(len(a)) #to print the length of a string
print(a)
print(a.upper()) #to uppercase the string
print(a.lower()) #to lowercase the string
print(a.rstrip('!')) # to strip the given assignment
print(a.replace("Sourav", "Kumar")) # to replace the existing string with another string
print(a.split(" ")) # to split the string

heading = "introduction To Python"
print(heading.capitalize()) # to capitalize the first letter of an string

str1= "welcome to the console!!!"
print(len(str1))
print(str1.center(50)) # to add the space in the string
print(a.count("Sourav")) # to count the given word
print(str1.endswith("!")) # to check the ending of an string

print(str1.endswith("to", 4, 10))

str1 = "He's name is sourav. He is good boy"
print(str1.find("iss")) # to fnd the string occurence if not find so it returns -1
print(str1.index("is")) # to fnd the string occurence if not find so it returns error

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # to check the string is alphanumeric or not (A-Z, a-z, 0-9)

str1 = "Welcome"
print(str1.isalpha()) # to check the string is alpha or not (A-Z, a-z)

str1 = "hello world"
print(str1.islower()) # to check the string is in lowercase or not

str1 = "hello world"
print(str1.isupper()) # to check the string is in uppercase or not

str1 = "sourav"
print(str1.isprintable()) # to check the string is printable or not

str1 = "  " # using spacebar
str2 = "  " # using tab
print(str1.isspace()) # to check the string contains the white spaces or not 
print(str2.isspace()) # to check the string contains the white spaces or not 

str1 = "World Health Organization"
print(str1.istitle()) # checks only if the first letter of the string is in uppercase or not

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python")) # check the string starts with given word or not

str1 = "Python is a Interpreted Language"
print(str1.swapcase()) # swaps the uppercase letter into lowercase and vice-versa

str1 = "His name is sourav. He is good boy"
print(str1.title()) # capitalize the each letter of teh word within the string'''

# if-else statement

# conditional operators
#>, <, >=, <=, ==, !=

'''a= int(input("Enter Your Age: "))
print("Your age is:", a)

if(a<18):
    print("No, you cannot drive")

else:
    print("Yes, you can drive")'''

#example 2

'''applePrice = 10
budget = 200

if(budget - applePrice > 50):
    print("Alexa, add 1 KG apples to the cart.")

else:
    print("ALexa, do not add apples to the cart.")'''

# elif statement

'''num = int(input("Enter the value of num: "))

if(num < 0):
    print("Number is Negative")

elif(num == 0):
    print("Number is Zero")

elif(num == 999):
    print("Number is Special")

else:
    print("Number is Positive")'''

# nested if statement

'''num = 18
if(num < 0):
    print("Number is Negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")

    elif(num > 10 and num <=20):
        print("Number is between 11-20")

    else:
        print("Number is greater than 20")

else:
    print("Number is Zero")'''
