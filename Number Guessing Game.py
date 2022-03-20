import random

top_of_range = input("Type a number:  ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than zero")
        quit()

else:
     print("Please enter a number")  
     quit() 

r = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number:  ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please enter a number:  ")  
        continue

    if user_guess == r:
        print("You got it right!!")
        break
    elif user_guess > r:
        print("You were above the number")
    else:
        print("You were below the number")

    
print("You got it in ", guesses, " guesses")