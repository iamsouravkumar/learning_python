# string formatting in python old versions.

letter= "Hey, my name is {1} and i am from {0}."
country= "India"
name = "Sourav"
print(letter.format(country,name))

# string formatting in python new versions - fStrings.

print(f"Hey, my name is {name} and i am from {country}.")
print(f"Hey, my name is {{name}} and i am from {{country}}.")

print(f"{2*30}")