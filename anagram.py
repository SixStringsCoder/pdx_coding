"""

>>> anagram('anagram', 'nag a ram')
True

>>> anagram('Right. One... two... five!', 'Three, sir.')
False

>>> anagram('My ideal time', 'Immediately')
True

>>> anagram('kdfjo *6 %4230', 'k3 df * %42oj0 6')
True

"""


import string


def anagram(annie, graham):
    """
    SOLUTION 3 ---> detect two words that are anagrams: use import string module then "short circuit" it,
    which uses list comprehension tucked into the function sorted()...not allocated memory just a list of
    instructions to do something with
    :param annie: 
    :param graham: 
    :return: boolean
    """
    new_annie = sorted(letter.lower() for letter in annie if letter in string.ascii_letters)

    new_graham = sorted(letter.lower() for letter in graham if letter in string.ascii_letters)

    print(new_annie)
    print(new_graham)



# def anagram(annie, graham):
#     """
#     SOLUTION 2 ---> detect two words that are anagrams: use import string module then "short circuit" it,
#     which uses list comprehension tucked into the function sorted()
#     :param annie:
#     :param graham:
#     :return: boolean
#     """
#     new_annie = [letter.lower() for letter in annie if letter in string.ascii_letters]
#     order_annie = sorted(new_annie)
#
#     new_graham = [letter.lower() for letter in graham if letter in string.ascii_letters]
#     order_graham = sorted(new_graham)
#
#     if order_annie == order_graham:
#         return True
#     else:
#         return False


# def anagram(annie, graham):
#     """
#     SOLUTION 1 ----> detect two words that are anagrams with sorted and replace method
#     :param annie:
#     :param graham:
#     :return: boolean
#     """
#
#     new_annie = sorted(annie.lower().replace(' ', ''))
#     new_graham = sorted(graham.lower().replace(' ', ''))
#
#     # annie_join = ''.join(new_annie)
#     # graham_join = ''.join(new_graham)
#
#     if new_annie == new_graham:
#         return True
#     else:
#         return False