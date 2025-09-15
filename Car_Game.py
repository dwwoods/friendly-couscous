user_input = ""
is_started = False
while True:
    user_input = input("> ").lower()
    if user_input == "help":
        print(""" 
start - to start the car
stop - to stop the car
quit - to quit the game""")
    elif user_input == "start":
        if is_started:
            print("The car is already Running")
        else:
            is_started = True
            print("car started...Ready to go!")
    elif user_input == "stop":
        if not is_started:
            print("The car is already Stopped")
        else:
            started = False
            print("car stopped.")
    elif user_input == "quit":
        print("Game Over")
        break
    else:
        print("I dont understand that")