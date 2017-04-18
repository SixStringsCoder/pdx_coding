"""
Write a function to decrypt an ROT13 Enconded message.

message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg."
"""

# Write your code here.

import string


def decoder():
    message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg.".lower()

    punct = string.punctuation
    space = string.whitespace

    decoded = ''
    for letters in message:
        if letters in punct or letters in space:
            decoded += letters
        else:
            if ord(letters) >= 110:
                correct = ord(letters) - 13
            elif ord(letters) <= 109:
                correct = ord(letters) + 26 - 13
            back_to_char = chr(correct)
            decoded += back_to_char

    return decoded


decoder()