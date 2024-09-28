# string methods in python

# Note - strings are immutable in python

a = "!!!Sourav!!! !!!!!! Kumar!!!!"
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
print(str1.title()) # capitalize the each letter of teh word within the string
