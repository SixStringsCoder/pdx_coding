"""
Check that a word follows "I before E except after C".

>>> check("recieve")
recieve doesn't follow the rule


>>> check("receive")
receive does follow the rule

>>> check("science")
science doesn't follow the rule

"""


def check(some_word):
    letter_i = 'i'
    letter_e = 'e'
    i_e_checker = str(some_word)

    if 'cie' in i_e_checker:
        print(f"{i_e_checker} doesn't follow the rule")
    elif 'cei' in i_e_checker:
        print(f"{i_e_checker} does follow the rule")
    else:
        print("Doesn't contain those letters.")

