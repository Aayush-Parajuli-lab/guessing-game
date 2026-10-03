import random

def Playround():
    print("Welcome to the Guessing Game !")

    secret = random.randint(1,10)
    attempt = 1

    while True:
        try:
            guess = int(input("Guess the number between 1 and 10 : "))
        except ValueError:
            print("Please enter a Whole number")
            continue
        if guess < secret:
            print("Too Low!")
        elif guess > secret:
            print("Too High !")
        else:
            print(f"You got it right in {attempt}. The secret was {secret} ")
            break


def main():
    while True:  # the game loop
        Playround()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


main()



