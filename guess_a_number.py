import random

computer_number = random.randint(1, 100)
attempts = 5

while attempts > 0:
    guess = input("Guess the number (1-100) in 5 attempts.")
    if not guess.isdigit():
        print("Invalid input. Try again...")
        continue

    player_number = int(guess)
    if player_number == computer_number:
        print("You guess it!")
        break
    elif player_number > computer_number:
        print("Too high!")
    else:
        print("Too low!")

if attempts == 0:
    print("You lose!")