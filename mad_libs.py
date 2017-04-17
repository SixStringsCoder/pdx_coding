"""

"""



def welcome(name):
    pipesL = "|" * 18
    pipesR = "|" * 16
    print("|" * 72)
    print(f"""{pipesL} Welcome, {name}, to Fantasy Mad Libs! {pipesR}""")
    print("|" * 72)

# Q to ask if person wants to play
def wanna_play():
    # welcome(name)
    oh_yeah = input("Are you ready to play a wild and crazy game of Mad Libs? Y/n ")
    if oh_yeah.lower() != "n":
        play()
    else:
        print("That's cool. Later alligator!")
        quit()

# function to do MadLib
def play():
    # create questions with variable to store answers

    male_celebrity = input("Name a male celebrity. ")
    female_celebrity = input("Name a female celebrity. ")
    noun_1 = input("Type a noun. ")
    noun_2 = input("Type another noun. ")

    pl_noun_1 = input("Type a plural noun. ")
    pl_noun_2 = input("Type another plural noun. ")
    pl_noun_3 = input("Type yet another plural noun. ")
    pl_noun_4 = input("I know you're sick of it but type one final plural noun. ")
    adj_1 = input("Type an adjective. ")
    adj_2 = input("You guessed it, type another adjective. ")
    place = input("Name a place. ")
    pl_profession = input("Name a plural profession. ")
    food_noun = input("Name a food item or dish. ")

    # print mad lib
    print(f"""
    Albert Einstein, the son of {male_celebrity} and {female_celebrity},
    was born in Ulm, Germany, in 1879. In 1902, he had a job
    as assistant {noun_1} in the Swiss patent office and attended
    the University of Zurich. There he began studying atoms, molecules,
    and {pl_noun_1}. He developed the theory of
    {adj_1} relativity, which expanded the phenomena of sub-atomic
    {pl_noun_2} and {adj_2} magnetism. In 1921,
    he won the Nobel prize for {pl_noun_3} and was director of
    theoretical {food_noun} at the Kaiser Wilhelm Institute in Berlin.
    In 1933, when Hitler became Chancellor of {place},
    Einstein came to America to take a post at Princeton Institute of
    {pl_noun_4}, where his theories about {pl_noun_4} helped America devise the first
    atomic {noun_2}. There is no question about it: Einstein was
    one of the most brilliant {pl_profession} of our time.
    """)

def play_again():
    again_answer = input("Do you want to play again? Y/n ")
    if again_answer.lower() != "n":
        play()
    else:
        print("Peace out!")



llama = input("What's your name, homey? ")
welcome(llama)
wanna_play()
play_again()

