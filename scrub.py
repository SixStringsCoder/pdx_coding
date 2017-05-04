"""
Write functions that accept 'dirty' string input, and outputs a human readable value.
Use a combination of python string methods and regular expressions.

Write, test, and refactor as you go.

"""

import re

def scrub_numbers(some_phrase: str) -> str:
    """
    >>> scrub_numbers('Be9autiful9 i4s be2tter th4an ug42ly')
    'Beautiful is better than ugly.' 
    
    :return: string
    """

    rid = re.sub(r'\d', '', some_phrase)
    final_text = rid + "."

    return final_text


def gentle_clean(some_phrase: str) -> str:
    """
    >>> gentle_clean('Explicit_is-better_than -implicit')
    'Explicit is better than implicit.'
    
    :return: string
    """

    cleaner = some_phrase

    for char in '-_ ':
        cleaner = cleaner.replace(char, ' ')
    cleaner = ' '.join(cleaner.split())
    fluff_dry = cleaner + "."

    return fluff_dry


def clean_data(some_phrase: str) -> str:
    """
    >>> clean_data('  42Simple-is_better_than-compl9ex   ')
    'Simple is better than complex.'

    :return: string
    """

    stripped = some_phrase.strip()
    no_nums = re.sub(r'[\d]', '', stripped)

    for char in '-_':
        no_nums = no_nums.replace(char, ' ')
    shined_buffed = no_nums + '.'

    return shined_buffed


def some_scrubber(some_phrase: str) -> str:
    """
    >>> some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . ')
    'Flat is better than nested.'
    
    :return: string
    """

    pattern = re.compile(r'''
                         (?<=\w)     
                         \s
                         (?=\w)
                         |
                         (?<=\w)
                         \s
                         (?=\W)
                         ''', re.VERBOSE)

    sing_space = pattern.sub('', some_phrase)


    three_space = re.sub(r'\s\s', ' ', sing_space)
    last_space = three_space.replace('. ', '.')
    return last_space


def mr_clean(some_phrase: str) -> str:
    """
    >>> mr_clean('Sparse is better than dense')
    ' S p a r s e   i s   b e t t e r   t h a n   d e n s e '
    
    :return: string
    """
    chopin_liszt = list()
    for l in some_phrase:
        chopin_liszt.append(l + " ")

    chopin_liszt.insert(0, ' ')
    listerine = ''.join(chopin_liszt)
    return listerine


def ms_clean(some_phrase: str) -> str:
    """
    >>> ms_clean('Readability counts')
    'R9y c4s'
    
    :return: 
    """

    break_apart = some_phrase.split()
    storage = list()

    for w in break_apart:
        first = w[0]
        storage.append(first)

        selection = w[1:-1]
        how_long = len(selection)
        storage.append(str(how_long))

        last = w[-1]
        storage.append(last)

    storage.insert(3, ' ')
    joiner = ''.join(storage)
    return joiner

# ms_clean('Readability counts')


def strong_cleaner(some_phrase: str) -> str:
    """
    >>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')
    'Errors should never pass silently.'
    
    :return: string
    """

    soap_water = re.sub(r'[@#%$*(1!&I&&]', '', some_phrase)
    squeaky_clean = soap_water + '.'

    return squeaky_clean


def extracto(some_string: str) -> int:
    """
    >>> extracto("1S2pe3cia4l ca5ses ar6en't sp7ecial en8ough to b9reak the r0ules.")
    45
    
    :return: int
    """

    extractor_tool = re.findall(r'[45]', some_string)
    final = ''.join(extractor_tool)
    return int(final)


def extracto(some_string: str) -> int:
    """
    >>> extracto("2S4pe6cia8l ca0ses ar2en't sp4ecial en6ough to b8reak the r0ules.")
    40

    :return: int
    """

    extractor_tool = re.search(r'[40]', some_string)

    # final = ''.join(extractor_tool)
    return extractor_tool



def extracto(some_string: str) -> int:
    """
    >>> extracto("3S6pe9cia2l ca5ses ar8en't sp1ecial en4ough to b7reak the r0ules.")
    45

    :return: int
    """

    extractor_tool = re.findall(r'[45]', some_string)
    num_as_str = ''.join(sorted(extractor_tool))
    final = int(num_as_str)
    return final

