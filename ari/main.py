import os
import chalk
from data_count import char_count, word_count, sent_count
from math import ceil


BOOKS = '/Users/mbp/Git/PythonFullStack/1_Python/3_Applied_Python/labs/ari/books/'


def output(score: int, file_name: str) -> None:
    """
    takes an integer stored in score, compares against dictionary of ages/levels and prints a text eval
    
    :return: None
    """
    ari_scale = {
        1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
        2: {'ages': '6-7', 'grade_level': '1st Grade'},
        3: {'ages': '7-8', 'grade_level': '2nd Grade'},
        4: {'ages': '8-9', 'grade_level': '3rd Grade'},
        5: {'ages': '9-10', 'grade_level': '4th Grade'},
        6: {'ages': '10-11', 'grade_level': '5th Grade'},
        7: {'ages': '11-12', 'grade_level': '6th Grade'},
        8: {'ages': '12-13', 'grade_level': '7th Grade'},
        9: {'ages': '13-14', 'grade_level': '8th Grade'},
        10: {'ages': '14-15', 'grade_level': '9th Grade'},
        11: {'ages': '15-16', 'grade_level': '10th Grade'},
        12: {'ages': '16-17', 'grade_level': '11th Grade'},
        13: {'ages': '17-18', 'grade_level': '12th Grade'},
        14: {'ages': '18-22', 'grade_level': 'College'}
    }

    score = ceil(score)
    look_up = ari_scale.get(score, ari_scale[14])

    grade_range, age_range = look_up['grade_level'], look_up['ages']

    decor_border = '-' * 62

    text_output = f"""
    The ARI for the file, {file_name.upper()}, is {score}.
    This corresponds to a {grade_range} level of difficulty
    that is suitable for an average person {age_range} years old.
    """

    chalk.cyan(decor_border)
    chalk.red(text_output)
    chalk.cyan(decor_border)


def compute_ari(text: str) -> int:
    """
    Compute the ARI for a given body of text loaded in from a file. Use external clean/count functions from file data_count.py
    
    :return: int
    
    """

    chars = char_count(text)
    words = word_count(text)
    sent = sent_count(text)

    score = 4.71 * (chars/words) + 0.5 * (words/sent) - 21.43
    return score


def file_opener(bookpath: str) -> str:
    """
    open text file
    
    :return: string
    """
    with open(bookpath, 'r') as file:
        text = file.read()  # .read is a method on a file object that returns the file as a single string
        return text


def book_catalog():
    """
    gather text file titles from path to a folder, offer user choice to pick a title, send that choice to 
    file_opener
    
    :return: None
    """

    book_list = [book for book in os.listdir(BOOKS) if '.txt' in book]
    menu_text = f"""To compute its automated readability index, 
pick from one of the files below:\n"""

    options = {index: book for index, book in enumerate(book_list, start=1)}
    options.update({'q)': 'quit'})

    chalk.green(menu_text)
    for index, book in options.items():
        print(f'{index}) {book}')

    choice = int(input("Enter number choice here >>> "))

    lookup_title =  options.get(choice)  # gets choice of text file title from book_list stores in lookup_title
    full_path = BOOKS + lookup_title     # concats BOOKS URL with text file name and stores in full_path
    text = file_opener(full_path)        # full text url path is passed to file_opener function to display text
    score = compute_ari(text)            # text passed to compute_ari where it's cleaned, counted and computed with ARI equation
    output(score, lookup_title)          # final output score and ranking printed to screen, pass text title name for final print out

book_catalog()
