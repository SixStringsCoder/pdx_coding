"""

>>> combine(7, 4)
11

>>> combine(42)
42

>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

>>> choose_longest("Greg", "Rooney")
'Rooney'

>>> choose_longest("Greg", "Rooney", "Philip", "Maximus", "Gabrielle")
'Gabrielle'

>>> choose_longest("Greg", [0, 0, 0, 0, 4])
[0, 0, 0, 0, 4]

"""


def combine(number, number2=0):
    """Return the Sum of _two or less_ elements using a default argument of zero."""
    return number + number2


def combine_many(*args):
    """Return the sum of any number of integers passed using *args."""
    return sum(args)


def choose_longest(*args):
    """Return the longest input argument."""

    def return_len(iter_length):
        return len(iter_length)

    return max(args, key=return_len)