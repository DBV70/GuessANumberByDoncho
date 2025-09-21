import random

computer_number = random.randint(1, 100)

while True:
    guess = input("Guess the number (1-100)")
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
