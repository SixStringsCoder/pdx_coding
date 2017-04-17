# import python's library to add functionality
import os
import random
import sys

# make a list of words
words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]


# CLEAR function to just clear a cluttered screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# WELCOME function
def welcome():
    # start the game... or exit
    start = input("Press ENTER/RETURN to start or Q to quit. ").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True

# DRAW function to make interface for game
def draw(bad_guesses, good_guesses, secret_word):
    clear()
    print("Welcome to the Letter Guessing Game!\n Guess the fruit I'm thinking of before you get 7 strikes!")
    print('')
    print('Strikes:\n {}/7'.format(len(bad_guesses)))
    print('')
    print("Wrong Letters")
    for letter in bad_guesses:
        print(letter, end=' ')
        print('\n')

        # heading plus draw spaces for the correct letters
        print("Secret Word")
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
                else:
                print('_ ', end='')

                print('')

# GET GUESS function and error msg
def get_guess(bad_guesses, good_guesses):
    while True:
        # take guess
        guess = input("Guess a letter: ").lower()
        # control input to one letter
        if len(guess) != 1:
            print(' ')
            print("Whoa, Nelly! Just guess one letter at a time!")
        # control same letter guessed twice
        elif guess in bad_guesses or guess in good_guesses:
            print(' ')
            print("You've already guessed that letter!")
        elif not guess.isalpha():
            print(' ')
            print("Letters, Dude! Just a, b, c....")
        else:
            return guess

# WIN LOSE PLAY AGAIN function
def play(done):
    # Play the game
    clear()
    # pick a random word from list
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            # print guessed letters
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False
            # print out win
            if found:
                print(' ')
                print("You win!")
                print("The word is '{}'!".format(secret_word))
                done = True
        else:
            # print missed letters
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You didn't guess it!")
                print("The secret word was '{}'.".format(secret_word))
                done = True

        if done:
            print(' ')
            play_again = input("Play again? Y/n ").lower()
            if play_again != "n":
                return play(done=False)
            else:
                print("See ya! Turn that frown upside down!")
                sys.exit()
done = False

while True:
    clear()
    welcome()
    play(done)