import random

val = random.randint(1, 100)
minval = 1
maxval = 100
while True:
    guess = input(f"Enter an integer between {minval} and {maxval}: ")
    if guess.isdigit():
        guess = int(guess)
        if guess == val:
            print("Congratulations!")
            break
        else:
            if guess < val:
                minval = guess
            else:
                maxval = guess
            print(f"Between {minval} to {maxval}")
    else:
        print("Please enter an integer")

