"""
# Test Data Below.  Leave these first two line alone.
>>> names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

>>> people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

# >>> evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

>>> evens = range(1, 21)


>>> long_names(names, 5)
['Kieran', 'Serada', 'Alfonzo']

>>> starts_with(names, 'S')
['Suki', 'Serada']

>>> last_names(people)
['Prasch', 'Ward', 'Balnik']

# >>> first_occ(people)
# [('Kieran', 'Instructor'), ('Alfonso', 'Student'), ('Fin', 'Student')]

>>> list_exp2(evens)
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

>>> smoosh(people)
['Kieran', 'Prasch', 'Instructor', 'Alfonzo', 'Ward', 'Student', 'Fin', 'Balnik', 'Student']

"""

from itertools import chain

def long_names(i, n):
    result = [name for name in i if len(name) >= n]
    return result


def starts_with(i, l):
    result = [name for name in i if name[0].upper() == l]
    return result


def last_names(i):
    last = [tupac[1] for tupac in i]
    return last


def first_occ(i):  #  return new tuple with first name and occupation
    name_occ = [(tupac[0], tupac[2]) for tupac in i]
    return name_occ


def list_exp2(i):  #  return list of evens squared
    expo = [even**2 for even in i if even % 2 == 0]
    return expo


def smoosh(i):     #  nest iterable inside another iterable or  2-dimensional list comprehension
    crazy = [item for person in i for item in person]
    return crazy


# def smoosh(i):   #  use itertools chain module to nest iterable inside another iterable
#     smasher = list(chain.from_iterable(i))
#     return smasher