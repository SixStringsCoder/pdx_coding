"""

>>> locate('l', 'hello')
[2, 3]

>>> locate('b', 'bannanas')
[0]

>>> locate('i', 'mississippi')
[1, 4, 7, 10]

"""


def locate(target, stringy_thing):
    """
    make use of enumerate number-generator to append target letter's index 
    number to new list 

    :return: list
    """

    new_list = list()

    for i, letter in enumerate(stringy_thing):
        if letter == target:
            new_list.append(i)

    return new_list



# def locate(target, stringy_thing):
#     """
#     list comprehension making use of enumerate number-generator to append target letter's index
#     number to new list
#
#     :return: list
#     """
#
#     new_list = [i for i, letter in enumerate(stringy_thing) if letter == target]
#
#     return new_list