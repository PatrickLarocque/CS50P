''' I'm thinking of a number between 1 and 100… '''

from random import randint

def main():
    # Accept user input until under inputs a valid positive integer. Else reprompt.
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                continue
            break
        except ValueError:
            continue
    guessing_game(level)

# Get a random number between 0 and level. Accept guesses from the user until the user guesses the target number. Reprompt invalid guesses.
def guessing_game(level):
    target = randint(1, level)
    guess = None
    while guess != target:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
        except ValueError:
            continue
        else:
            if guess < target:
                print("Too small!")
            elif guess > target:
                print("Too large!")
            else:
                print("Just right!")


if __name__ == "__main__":
    main()