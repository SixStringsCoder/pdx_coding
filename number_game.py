import random


def lets_play_homey():
    num_tries = 0
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    while True:
        # get a number guess from player
        guess = int(input("Guess a number between 1 and 10. "))
        num_tries += 1
        # compare player's guess to secret number
        if guess == secret_num and num_tries <= 2:
            # print hit or miss
            print("Good guess, Nostradomus! The number is indeed {}!".format(secret_num))
            break
        # too low
        elif guess < secret_num and num_tries < 5:
            print("Go higher... Try again.")
            continue
        # too high
        elif guess > secret_num and num_tries < 5:
            print ("Go lower... Try again.")
            continue
        else:
            print("Game Over. The number is {}.".format(secret_num))
            break


def play_again():
    decider = input("Play again? Y or N.")
    if decider == "Y":
        lets_play_homey()
    else:
        print("See ya!")


lets_play_homey()
play_again()