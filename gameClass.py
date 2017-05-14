"""
This file was written by Steve Hanlon.

The object of the game is to make matches of similar cards/flashcards until no more matches can be made
"""

import random


class Matching:
    def __init__(self, name: str, deck=2):
        self.name = name

        fl_cards = ['cat', 'dog', 'bird', 'lizard', 'snake', 'hippo', 'fish', 'horse', 'elephant', 'camel']

    def repr(self):
        msg = f"Matching ({name})"
        return msg

    def __str__(self):
        return f"Matching pairs of {name} activity."

    def flashcards(self, vocabulary: list) ->list:
        fl_cards = list(vocabulary)
        return flashcards

    def shuffle(self):
        mix_em_up =