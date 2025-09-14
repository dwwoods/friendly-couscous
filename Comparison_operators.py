#temperature = 30

#if temperature >= 30:
    #print("It's a hot day")

#else:
    #print("It's a not hot day")

#!= not equal
#== exaclty

name = input("What is your name?")

print(len(name))

if len(name) < 3:
    print("Name is too short")
elif len(name) > 50:
    print("Name is too long")
else:
    print("Name looks good")