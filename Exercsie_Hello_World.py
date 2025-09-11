#you cant mix type in functions - here was an int and string.  You use converting functions

#birth_year = input("Birth year: ") # input *always* gives you a string
#print(type(birth_year)) # this tells you the type
#age = 2025 - int(birth_year)
#print(type(age))
#print(age)

#Exercise
#ask a user for their weight in lbs and convert it to kilograms and print that figure on the terminal

weight_lbs = input("What is your weight, in pounds? ")
print(type(weight_lbs))
weight_kgs = float(weight_lbs) / 2.2
print(weight_kgs)