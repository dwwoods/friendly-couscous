#i = 1
#while i <= 5:
#    print("he" * i)
#    i = i + 1
#print("--- done ---")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess my number 0-9: '))
    guess_count += 1
    if guess == secret_number:
        print('You guessed it!')
        break
else:
    print('Sorry, that\'s wrong, try again!')