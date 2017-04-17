"""
created by Steve Hanlon

Make a function that advises a player on the best next move in a round of blackjack.
For now, just use 15 as a Hit/Stay Threshold.  Feel free to add testable features.

>>> advise_player(10, 5)
15 Hit.

>>> advise_player('Q', 5)
15 Hit.

>>> advise_player('A', 'K')
21 Blackjack!

>>> advise_player('J', 'K')
20 Stay.


"""

def advise_player(card1, card2):
    royalty = 'KQJ'
    ace = 'A'

    try:
        card1 =  int(card1)
    except ValueError:
        if card1 in royalty:
            card1 = 10
        elif card1 in ace:
            card1 = 11

    try:
        card2 =  int(card2)
    except ValueError:
        if card2 in royalty:
            card2 = 10
        elif card2 in ace:
            card2 = 11

    total = int(card1) + int(card2)

    if total <= 15:
        print(f"{total} Hit.")

    if total == 21:
        print(f"{total} Blackjack!")

    if total > 15 and total < 21:
        print(f"{total} Stay.")

