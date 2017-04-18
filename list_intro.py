"""
>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> spell_out(a)
m
u
s
i
c

>>> spell_out(b)
17
28
42
31
12

>>> first_and_last(b)
17
12

>>> first_and_last(a)
m
c

"""

def spell_out(a):
    for char in a:
        print(char)


def first_and_last(b):
    print(b[0], b[-1], sep='\n')