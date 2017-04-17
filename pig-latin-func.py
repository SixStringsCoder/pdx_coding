# Practice: Pig Latin Refactor

"""
Convert your [Pig Latin Practice](/practice/pig-latin.md) to use functions.

Break each step into a separate function with explicit input arguments and
output return value, use a main which pipes data through all of the steps, and properly name functions.

If you find a better way to structure your code through this process, please use it!
No need to keep exactly the same solution steps as before.
"""


def piggy_talk(pig_word):
    """
    
    :param pig_word: 
    :return: w ord translated into pig latin
    """

    vowels = 'aeiou'
    con_end = 'ay'
    vow_end = 'yay'
    first_letter = pig_word[0]                         # first_letter of the word
    #break into a list

    if pig_word[0] not in vowels: #if consonant
        p_latin_word = pig_word[1:] + "{}{}".format(first_letter, con_end)      # exclude it and append it on end with 'ay'
        if pig_word[0].upper():                        # if capital consonant
            p_latin_word = pig_word[1].upper() + pig_word[1:]+ "{}{}".format(first_letter.lower(), con_end) # keep 1st letter capital, add 'ay'

    if pig_word[0] in vowels or len(pig_word) < 2:   # if first letter is a vowel
        p_latin_word = pig_word + "{}".format(vow_end) # keep vowel add 'yay'

    print(p_latin_word, end=" ")



def piggy_phrase(pig_sentence):
    splitter = pig_sentence.split()
    return splitter


def phrase():
    phrase_choice = input("Write a short sentence to translate?  >>")
    piggy_list = piggy_phrase(phrase_choice)
    for words in piggy_list:
        piggy_talk(words)


def word():
    word_choice = input("Give me a word to translate?  >>")
    piggy_talk(word_choice)



phrase()