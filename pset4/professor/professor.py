'''
Implement a program that:

1. Prompts the user for a level n. If the user does not input 1, 2, or 3, the program should prompt again.
2. Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits. 
No need to support operations other than addition (+).
3. Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output 
EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered 
correctly after three tries, the program should output the correct answer.
4. The program should ultimately output the user's score: the number of correct answers out of 10.
'''
from random import randint

def main():
    level = get_level()
    score = 0
    # Loop through 10 rounds of addition problems.
    for _ in range(1, 11):
        x = generate_integer(level)
        y = generate_integer(level)
        # Up to 3 attempts per problem.
        for attempt in range(1, 4):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer != x + y and attempt <= 2:
                    raise ValueError
                # Third unsucessful attempt, solution is revealed. No score for this round.
                elif answer != x + y and attempt == 3: 
                    print((f"{x} + {y} = {x + y}"))
                    raise ValueError
                # Answer was correct. 1 point.
                else:
                    score += 1
                    break
            except ValueError:
                print("EEE")
    # Print the total score after 10 rounds.
    print(f"Score: {score}")

# Determines the amount of digits in each random number.
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in range(1, 4):
                raise ValueError
            return level
        except ValueError:
            continue

# Generates random numbers 'level' digits long.
def generate_integer(level):
    if level == 1:
        return randint(0, 10)
    range_start = 10**(level-1)
    range_end = (10**level)-1
    return randint(range_start, range_end)

if __name__ == "__main__":
    main()