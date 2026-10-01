import random

print("Welcome to the Guessing Game !")

secret = random.randint(1,10)
guess = int(input("Guess the number between 1 and 10 : "))

if guess == secret:
    print("Correct you win!")
else:
    print(f"wrong the Correct number was {secret} ")

