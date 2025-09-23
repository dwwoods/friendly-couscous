def greet_user(first_name, last_name): # rather than () we put a function in i.e (first_name)
    print(f"Hi {first_name}, {last_name}")
    print("Welcome aboard.")


print("---start---")
greet_user("Paul", "Smith") # these are positional arguments
greet_user(last_name="Mary", first_name="Shelly" ) # these are keyword arguments - sometimes help with readability of code
#keyword arguments improve arguments that involve numbers
# order is postional argument then keyword
print("---end---")



