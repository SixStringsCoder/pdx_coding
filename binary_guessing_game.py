import random


def binary_guess(guesses_allowed, low_num, high_num, correct_num):
    """
    computer makes based on binary search, initated by randomint

    :return: integer
    """

    num_guesses = 0

    print("HAL, do you read me?")
    print(f"Affirmative, Dan.")
    print()
    input(f"HAL, guess the number I'm thinking. It's between {low_num} and {high_num}.  >>>>> HIT RETURN")

    # comp_guess = int(high_num / 2)
    comp_guess = random.randint(low_num, high_num)
    print()
    print(f'Is the number {comp_guess}, Dan?')

    while guesses_allowed != 0:
        guesses_allowed -= 1
        num_guesses += 1

        if comp_guess == correct_num:  # CORRECT
            print(f'You got it, HAL! The number is {correct_num}!  You guessed it in {num_guesses} tries.')
            print()
            break

        elif comp_guess < correct_num:  # TOO LOW
            print(f'Too low, HAL. Guess higher. --------------{num_guesses} guess---{low_num} low---{high_num} high')
            print()
            low_num = comp_guess
            comp_guess = int((high_num + low_num) / 2)

        elif comp_guess > correct_num:  # TOO HIGH
            print(f'Too high, HAL. Guess lower. --------------{num_guesses} guess---{low_num} low---{high_num} high')
            print()
            high_num = comp_guess
            comp_guess = int((high_num + low_num) / 2)

        print(f'Is the number {comp_guess}, Dan? ------------{low_num} low---{high_num} high')

    print(f'Sorry, HAL! The number is {correct_num}!')



binary_guess(16, 1, 100000, 23987)




#
# import random
#
#
# def binary_guess(guesses_allowed, low_num, high_num, correct_num):
#     """
#     computer makes random guesses but does not strategize based on passed mistakes
#
#     :return: integer
#     """
#
#     num_guesses = 0
#     print("HAL, do you read me?")
#     print(f"Affirmative, Dan.")
#     print()
#     input(f"HAL, guess the number I'm thinking. It's between {low_num} and {high_num}.  >>>>> HIT RETURN")
#     comp_guess = random.randint(low_num, high_num)
#     print()
#     print(f"Is the number {comp_guess}, Dan?")
#
#     while guesses_allowed != 0:
#         guesses_allowed -= 1
#         num_guesses += 1
#
#
#         if comp_guess < correct_num:                                                                    #TOO LOW
#             measure = input(f'Too low, HAL. Guess higher. {guesses_allowed}--{num_guesses}')
#             comp_guess = random.randint(comp_guess, high_num)
#             # print(f"Is the number {comp_guess}, Dan?")
#
#         elif comp_guess > correct_num:                                                                  #TOO HIGH
#             measure = input(f'Too high, HAL. Guess lower. {guesses_allowed}--{num_guesses}')
#             comp_guess = random.randint(low_num, comp_guess)
#             # print(f"Is the number {comp_guess}, Dan?")
#
#         elif comp_guess == correct_num:                                                                 #CORRECT
#             print(f"You got it, HAL! The number is {correct_num}!  You guess it in {num_guesses}.")
#
#         print(f"Is the number {comp_guess}, Dan?")
#
#     print(f"Sorry, HAL! The number is {correct_num}!")
#
#
# binary_guess(16, 1, 1000, 373)