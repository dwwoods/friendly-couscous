#passing info to functions
def greet_user(first_name, last_name): # rather than () we put a function in i.e (first_name)
    print(f"Hi {first_name}, {last_name}")
    print("Welcome aboard.")


print("---start---")
#greet_user() will return an error - if we define a parameter we must use it
#agrguments are the value supplied to a funcion i.e. "paul" and "mary" in this case
greet_user("Paul", "Smith")
greet_user("Mary", "Shelly" )
print("---end---")



