"""
>>> letters = [['a', 'b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i']]

>>> denest(letters)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
"""

from itertools import chain


def denest(i):
    """
    This list comprehension is doing the same thing as the
    nested FOR loop with .append()

    :return: list
    """

    new_list = [word for sub_list in i for word in sub_list]

    return new_list


# def denest(i):
#     """
#     These nested FOR loops is doing the same thing as the
#     list comprehension below
#
#     :return: list
#     """
#     new_list = list()
#     for sub_list in i:
#         for word in sub_list:
#             new_list.append(word)
#     return new_list



# def denest(i):
# """
# Uses from itertools import chain
# """
#     flattened = list(chain.from_iterable(i))
#     return flattened



# def denest(i):
# """
# Another nested FOR loop
# """
#     flattened = [item for let_list in i
#                  for item in let_list]
#     return flattened






