"""
use data_count as an import into main.py with ARI score lab.  These function count characters, words and sentences
and main.py uses their return values to calculate ARI score

"""


import re


def char_count(text: str) -> int:
    """
    >>> char_count("Red touching black is a friend of Jack, Red touching yellow can kill a fellow.")
    62
    
    count characters excl. spaces and punct of some text input
    
    :return: int
    """
    chars = re.sub(r'[,.\s\'()]', '', text.lower())
    chars_count = len(chars)
    return chars_count


def word_count(text: str) -> int:
    """
    >>> word_count("Red touching black is a friend of Jack, Red touching yellow can kill a fellow.")
    15
    
    count words of some text input

    :return: int
    """
    words = re.sub(r'[,.\'()]', '', text.lower())
    words_list = words.split()
    words_count = len(words_list)
    return words_count


def sent_count(text: str) -> int:
    """
    >>> sent_count("Red touching black is a friend of Jack. Red touching yellow can kill a fellow.")
    2

    count sentences of some text input, split at period...need to tweak for stanzas AND sentences.

    :return: int
    """
    sent_list = text.split('.')
    sent_list.remove('\n')
    sent_count = len(sent_list)
    return sent_count

