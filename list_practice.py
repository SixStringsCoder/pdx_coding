"""
Given an input list, return it in reverse.
>>> backwards([56, 57, 58, 59, 60])
[60, 59, 58, 57, 56]


Find the max number in a given list.  Then, change every element in the list containing the first number of the maximum to the maximum number.
>>> maximus([56, 57, 58, 59, 60])
[60, 57, 58, 59, 60]

>>> maximus([56, 67, 56, 59, 60])
[67, 67, 67, 59, 67]


Given two lists, return True if the first two items are equal.
>>> compare_first_element(['migratory', 'birds', 'fly', 'south'], ['migratory', 'monopoloy', 'mind'])
True
>>> compare_first_element([7, 10, 11, 102], ['7', '10', '11', '102'])
False


Return True if the first letter of the second element in each list is equal. (Case Insensitive)
>>> compare_second_letter(['migratory', 'penguins', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
True

>>> compare_second_letter(['migratory', 'birds', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
False


Given two lists, return one list, with all of the items of the first list, then the second
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'])
['mama', 'llama', 'baba', 'yaga']


Use a default argument to allow the user to reverse the order!
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'], reverse=True)
['yaga', 'baba', 'llama', 'mama']


"""


def backwards(iterable):
    """
    objective: Reverse the input iterable and return it
    :param iterable: 
    :return: iterable reversed
    """
    response = iterable[::-1]
    return response




def maximus(iterable):
    """
    objective: Find the max number in a given list. Then, change every element 
    in the list containing the first number of the maximum to the maximum number.
    :param iterable: 
    :return: new list with altered values based around max value
    """
    new_iter = []                       # Empty list to hold new list of values
    big_num = max(iterable)             # Find max value in iterable argument
    big_str = str(big_num)              # Convert max value to a string

    for i in iterable:
        stringify = str(i)              # Change each ints to strings

        if big_str[0] in stringify:     # Check if max string[0] is present in each string values
            new_list_item = big_num     # Yes,string value is present. Change that string value to max value
        else:
            new_list_item = i           # No, it's not present. Leave "i" alone

        new_iter.append(new_list_item)  # Append the iterations to new list

    return new_iter                     # Return the list


def compare_first_element(list1, list2):
    """
    objective: compare first item of 2 lists for a match
    :param list1: 
    :param list2: 
    :return: boolean
    """
    if list1[0] == list2[0]:
        return True
    else:
        return False


def compare_second_letter(list1, list2):
    """
    objective: compare first letter of second element in 2 lists for match
    :param list1: 
    :param list2: 
    :return: boolean
    """
    l1 = list1[1].lower()
    l2 = list2[1].lower()

    if l1[0] == l2[0]:
        return True
    else:
        return False


def smoosh(list1, list2, reverse=False):
    """
    objective: return one list, with all of the items of the first list, then the second. 
    If reverse, use a default argument to allow the user to reverse the order!
    :param list1: 
    :param list2: 
    :param reverse: 
    :return: concatenated list
    """
    smooshed = list1 + list2
    if reverse:
        smooshed.reverse()
    return smooshed