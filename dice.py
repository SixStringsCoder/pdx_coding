# dice.py

## Objective
"""
Write a simple program that, when run, prompts the user for input then prints a result.

Program should ask the user for the number of dice they want to roll as well as the number of sides per die.

1. Open Atom
1. Create a new file and save it as `dice.py`
1. Follow along with your instructor

------

## Key Concepts

- Variables
- String concatenation
- Handling user input
- Importing functions
- Defining functions
- `for` loops¹
- The `range` statement¹
- Casting values
- Reading error messages

------

Sources:

1. [Compound statements](https://docs.python.org/3/reference/compound_stmts.html)

"""
import random


def die_roll(dice, sides):
    for die in range(0, int(dice)):
        roll = random.randint(1, int(sides))
        print(roll)


def answers():
    num_die = input("How many die do you want to roll? ")
    num_sides = input("How many sides does your die have? ")
    die_roll(num_die, num_sides)


answers()