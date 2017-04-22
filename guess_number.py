"""
created by Steve Hanlon 2017

'Guess The Number'
1. Display a welcome screen to the user.
2. use random module to choose a random number between 1 and 2 billion.
3. After the computer chooses a number, the human attempts to guess the computer's secret number in as few guesses as possible.
4. Option to make multi-level connected to number of guesses

Style: import chalk to alter terminal display

"""


import random


def randy_num(level_tries):
    chosen = random.randint(1, 2000000000)
    pick = int(input("Guess a number between 1 and 2 billion.\n Type it here without commas  >> "))
    guesses = 0

    while guesses < level_tries:
        guesses += 1
        if pick < chosen:
            pick = int(input(f"Too low! Guess higher!---[Guess Count = {guesses}] >> "))
        elif pick > chosen:
            pick = int(input(f"Too high! Guess lower!---[Guess Count = {guesses}] >> "))
        elif pick == chosen:
            input(f"That's it! The number is {pick}. You got it in {guesses} attempt(s)!")
            break
    else:
        input(f"Game over. The number is {chosen}")


def welcome():
    level = int(input("""Welcome to the Land of Guesses\n 
    Play Level 1, 2 or 3 >>> """))

    if level == 1:
        print("You get 5 tries to guess the number.")
        randy_num(5)
    elif level == 2:
        print("You get 10 tries to guess the number.")
        randy_num(10)
    else:
        print("You get 16 tries to guess the number.")
        randy_num(16)


welcome()