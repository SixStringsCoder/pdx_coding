"""

>>> exclude_em([56, 57, 58, 59, 60], 57)
[56, 59, 60]

>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34], 456)
[43, 67, 878, 5, 65, 34]

>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34])
[456, 23, 878, 5, 65, 34]

>>> double([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0])
[86, 67, 456, 46, 1756, -1, -1, -1]

>>> punch_in([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0], 2)
[43, 67, 2, 1, 1, 2, 2, 0, 0, 0, 456, 23, 878, 5, 65, 34]

>>> punch_in([56, 57, 58, 59, 60], [0, 0, 0, 0, 0], 4)
[56, 57, 58, 59, 0, 0, 0, 0, 0, 60]

punch_in(['Hey', 'Hey', 'Hey'], ['Joe', 'Joe', 'Joe'], 2)

"""


def exclude_em(liszt, num_excl=None):
    """
    Given a `list`, exclude an input integer `n` (2nd param), and its following element.
    :param liszt: 
    :param num_excl: 
    :return: list
    """

    if num_excl:
        here = liszt.index(num_excl)
        del liszt[here:here+2]

    else:
        liszt = liszt[2:]

    return liszt




def double(list_int1, list_int2):
    """
    two `list`s of `int`s, multiply numbers located at the same index by one another 
    and append them to a new list. If the result is `0`, append `-1` instead of `0`.  
    finally, 
    :param list_int1: 
    :param list_int2: 
    :return: new list
    """

    new_list = []

    for l1, l2 in zip(list_int1, list_int2):
        mult_result = l1 * l2
        new_list.append(mult_result)
        if mult_result == 0:
            new_list.remove(0)
            new_list.append(-1)
    return new_list




def punch_in(itty1, itty2, position):
    """
    Given two `list`s and an `int`, insert the elements of the 2nd list into the first list at the nth position (int).
    :param itty1: 
    :param itty2: 
    :param position: 
    :return: mutated list
    """

    for i in itty2:
        itty1.insert(position, i)
        position += 1

    return itty1



def punch_in(itty1, itty2, position):
    """
    second solution using slicing
    Given two `list`s and an `int`, insert the elements of the 2nd list into the first list at the nth position (int).
    :param itty1: 
    :param itty2: 
    :param position: 
    :return: mutated list
    """

    itty1[position:position] = itty2    # use zero-width slicing by starting and stopping at same index position

    return itty1

