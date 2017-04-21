#
# # Lab: Magic Ball
#
# ###### Delivery Method: Prompt and Demo
#
# --------------
#
# ##### Goal
#
# Write a test-based Python game to simulate a classic "Magic Eight Ball".
#
# --------------------
#
# ##### Instructions
#
# 1. If you are not familiar with the magic 8 ball idea, check out the wiki! [Magic 8 Ball Wiki](https://en.wikipedia.org/wiki/Magic_8-Ball)
#
#
# 1. Print a welcome screen to the user.
# 1. use the random module's `random.choice()` to choose a prediction (or with your own clever logic).
# 1. Display the result of the 8 ball.
# 1. Ask the user if they want to play agian.
# 1. Say Goodbye on exit.
# -------------------
#
# #### Documentation
#
# 1. [Python Official: Random: `random.choice()`](https://docs.python.org/3/library/random.html#random.choice)
#
# ----------------------
#
# #### Key Concepts
#
# - Event Loops
# - User I/O
# - Random Module


import random


top_structure = '^*'
bot_structure = '_*'
choices = ["It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"]


def adios_amigo():
    def curtain():
        print(top_structure * 8)
        print("<< GOODBYE >>")
        print(bot_structure * 8)
        print()

    curtain()
    print("A good-bye is never painful unless you're never going to say hello again.")

    quit()


def ask_again():
    again = input("Would you like to ask another question? ➽ Y/n ")
    print()
    if again != 'n'.lower():
        ask()
    else:
        adios_amigo()


def answer():
    pick = random.randint(0, len(choices))
    print()
    print(choices[pick])

    ask_again()


def ask():
    print()
    question = input("What do you want to ask the Magic Ball? ")
    answer()


def welcome():
    print(top_structure * 8)
    print("<< MAGIC BALL >>")
    print(bot_structure * 8)
    print()

    name = input("What do you call yourself? ")
    print()
    print(f"Welcome, {name.capitalize()}!")
    print()
    consult = input("Do you want to consult the Magic Ball? ➽ Y/n ")
    print()
    if consult != 'n'.lower():
        ask()
    else:
        adios_amigo()


welcome()
ask()