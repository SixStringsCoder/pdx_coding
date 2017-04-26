"""

#  Leave the line below alone, it is test data.
>>> llamas = [45, 37, 96, 23, 55, 2, 0, 88, 0, 45, 0, 345, 1, 76, 45, 34, 87]

>>> kangas = [1000, -3, 106, 0, 5, 20, -1, 88, 0, 5, 1, 78.345, -34, 870]

>>> apply_to_all(llamas, 2)
[90, 74, 192, 46, 110, 4, 176, 90, 690, 2, 152, 90, 68, 174]

>>> apply_to_all(kangas, 4)
[4000, 424, 20, 80, 352, 20, 4, 313.38, 3480]

"""


def apply_to_all(it, multi_by):
    """
    Using list comprehension with same flow as example below.
    :param it: list with integers
    :param multi_by: an integer to multiply elements in list parameter by
    :return: 
    """
    new_list = [elem * multi_by for elem in it if elem > 0]

    return new_list




# def apply_to_all(it, multi_by):
#     """
#     FOR conditional with append to new list
#     :param it: list with integers
#     :param multi_by: an integer to multiply elements in list parameter by
#     :return: list
#     """
#
#     new_list = list()
#
#     for elem in it:
#         new = elem * multi_by
#         if new > 0:
#             new_list.append(new)
#
#     return new_list


