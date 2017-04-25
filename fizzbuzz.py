"""

>>> fizz_buzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

REMEMBER: Use Encapsulation! D.R.Y.
>>> joined_buzz(15)
'1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz'

"""


def fizz_buzz(n):
    """
    Fizz Buzz list builder with all string elements
    :param n: 
    :return: list
    """
    fizzy_lister = []
    c = 1

    while c <= n:
        if c % 3 == 0 and c % 5 == 0:
            fizzy_lister.append('FizzBuzz')
        elif c % 5 == 0:
            fizzy_lister.append('Buzz')
        elif c % 3 == 0:
            fizzy_lister.append('Fizz')
        else:
            fizzy_lister.append(str(c))
        c += 1

    return fizzy_lister


def joined_buzz(n):
    """
    FizzBuzz using list building then string join
    :param n: 
    :return: string
    """
    fizzy_lister = []
    c = 1

    while c <= n:
        if c % 3 == 0 and c % 5 == 0:
            fizzy_lister.append('FizzBuzz')
        elif c % 5 == 0:
            fizzy_lister.append('Buzz')
        elif c % 3 == 0:
            fizzy_lister.append('Fizz')
        else:
            fizzy_lister.append(str(c))
        c += 1
    string0rama = ' '.join(fizzy_lister)

    return str(string0rama)


# def joined_buzz(n):
#     """
#     FizzBuzz using IFs and no ELIFs
#     :param n:
#     :return: string
#     """
#     #     fizzy_lister = list()
#     c = 1
#
#     while c <= n:
#         item = str()
#         if c % 3 == 0:
#             item += 'Fizz'
#         if c % 5 == 0:
#             item += 'Buzz'
#         else:
#             item = str(c)
#
#         fizzy_lister.append(item)
#
#         c += 1
#
#     string0rama = ' '.join(fizzy_lister)
#
#     # print("'" + string0rama + "'")
#     return string0rama


# def joined_buzz(n):
#     """
#     FizzBuzz using just string building
#     :param n:
#     :return: string
#     """
#     fizzy_buzz_string = ''
#     c = 1
#
#     while c <= n:
#         if c % 3 == 0 and c % 5 == 0:
#             fizzy_buzz_string += 'FizzBuzz'
#         elif c % 5 == 0:
#             fizzy_buzz_string += 'Buzz '
#         elif c % 3 == 0:
#             fizzy_buzz_string += 'Fizz '
#         else:
#             fizzy_buzz_string += str(c) + ' '
#         c += 1
#
#     print("'" + fizzy_buzz_string + "'")