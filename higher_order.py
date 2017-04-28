"""
>>> numbers = [2, -4, -6, 7,-9, 1, 9, -2, -3, 6]

>>> sorted_absolute(numbers)
[1, 2, -2, -3, -4, -6, 6, 7, -9, 9]

>>> quote = "In the end, it's concluded that the airspeed velocity of a (European) unladen swallow is about 24 miles per hour or 11 meters per second. But, the real question is not about swallows at all."

>>> shortest_to_longest(quote)
['a', 'In', 'of', 'is', '24', 'or', '11', 'is', 'at', 'the', 'the', 'per', 'per', 'the', 'not', 'end,', "it's", 'that', 'hour', 'But,', 'real', 'all.', 'about', 'miles', 'about', 'meters', 'unladen', 'swallow', 'second.', 'airspeed', 'velocity', 'question', 'swallows', 'concluded', '(European)']

>>> sort_last_char(quote)
['(European)', 'end,', 'But,', 'second.', 'all.', '11', '24', 'a', 'concluded', 'airspeed', 'the', 'the', 'the', 'of', 'real', 'In', 'unladen', 'question', 'per', 'hour', 'or', 'per', "it's", 'is', 'miles', 'meters', 'is', 'swallows', 'that', 'about', 'not', 'about', 'at', 'swallow', 'velocity']

>>> double(numbers)
[4, -8, -12, 14, -18, 2, 18, -4, -6, 12]

>>> all_upper(quote)
['IN', 'THE', 'END,', "IT'S", 'CONCLUDED', 'THAT', 'THE', 'AIRSPEED', 'VELOCITY', 'OF', 'A', '(EUROPEAN)', 'UNLADEN', 'SWALLOW', 'IS', 'ABOUT', '24', 'MILES', 'PER', 'HOUR', 'OR', '11', 'METERS', 'PER', 'SECOND.', 'BUT,', 'THE', 'REAL', 'QUESTION', 'IS', 'NOT', 'ABOUT', 'SWALLOWS', 'AT', 'ALL.']

>>> positive(numbers)
[2, 7, 1, 9, 6]

Filter words longer than 3, make all words lowercase words, and sort by last letter.
>>> lower_last_longwords(quote)
['(european)', 'end,', 'but,', 'second.', 'all.', 'concluded', 'airspeed', 'real', 'unladen', 'question', 'hour', "it's", 'miles', 'meters', 'swallows', 'that', 'about', 'about', 'swallow', 'velocity']

"""


def sorted_absolute(merry_pranksters):
    """sort by absolute value"""
    the_bus = sorted(merry_pranksters, key=abs)
    return the_bus


def shortest_to_longest(prose):
    """sort list short to long...use key function in a higher order function"""
    prose_list_maker = prose.split(' ')
    sorted_list = sorted(prose_list_maker, key=len)
    return sorted_list


def sort_last_char(prose):
    """sort list short to long using last char in each element...use key function in a higher order function"""
    prose_list_maker = prose.split(' ')

    # """alternative way using Lambda anonymous Function"""
    # sorted_list = sorted(prose_list_maker, key=lambda word: word[-1])

    def last_letter(word):  # key function
        return word[-1]

    sorted_list = sorted(prose_list_maker, key=last_letter)

    return sorted_list


def double(list_of_numbers):
    """double each digit in list"""
    doubled = [dig + dig for dig in list_of_numbers]
    return doubled


def all_upper(prose):
    """make all uppercase use list comp"""
    prose_list_maker = prose.split(' ')

    movin_on_up = [word.upper() for word in prose_list_maker]
    return movin_on_up


def positive(unwanted):
    """filter out all negative integers from list"""
    def exclude(num):
        if num >= 0:
            return True
        else:
            return False

    elite = list(filter(exclude, unwanted))
    return elite

    # """alternative way using list comp"""
    # elite = [citizen for citizen in unwanted if citizen >= 0]
    # return elite


def lower_last_longwords(prose):
    """make remove elements > 3 chars, lowercase them and sort by last char....try High order func + key func and also lambda variety"""
    prose_list_maker = prose.split(' ')

    basic_training = [word.lower() for word in prose_list_maker if len(word) > 3]

    # """alternative way using help function"""
    # def helper(word):
    #     return word[-1]
    #
    # in_shape = sorted(basic_training, key=helper)
    # return in_shape

    in_shape = sorted(basic_training, key=lambda word: word[-1])
    return in_shape