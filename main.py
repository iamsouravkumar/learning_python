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


# # variables and data types

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

# operators in 

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

fruit = 'mango'
print(fruit[0:4])
print(len(fruit))
print(fruit[-3:-1])
print(fruit[-4:-2])