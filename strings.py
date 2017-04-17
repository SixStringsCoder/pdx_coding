"""
Return the number of letter occourances in a string.
>>> count_letter('i', 'Antidisestablishmentterianism')
5
>>> count_letter('p', 'Pneumonoultramicroscopicsilicovolcanoconiosis')
2


Return the letter that appears last in the engligh alphabet.
>>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
'the latest letter is v.'


Convert input strings to lowercase without any surrounding whitespace.
>>> lower_case("SUPER!")
'super!'
>>> lower_case("        NANNANANANA BATMAN        ")
'nannananana batman'

"""

def count_letter(letter, some_string):
    string_o_scope = some_string.lower().count(letter)
    return string_o_scope

def latest_letter(word):
    last_place = max(word)
    final_sentence = f'the latest letter is {last_place}.'
    return final_sentence

def lower_case(uppercase_word):
    humbler = uppercase_word.lower().strip()
    return humbler