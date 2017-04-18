"""

>>> together('knights', 'camelot')
k c
n a
i m
g e
h l
t o
s t

>>> together('princess', 'chambers')
p c
r h
i a
n m
c b
e e
s r
s s

>>> together(['a', 'b', 'c', 'd', 'e'], ['Ay', 'Bad', 'SeeYa', 'Duh', 'Eh'])
a Ay
b Bad
c SeeYa
d Duh
e Eh


"""


# def together(arg1, arg2):
#     for a, b in zip(arg1, arg2):              # Unpack the tuple with a and b which represent out put values of zip
#         print(a, b)


# def together(arg1, arg2):
#     for elements in range(0, len(arg1)):      # Elements is representing numbers of range
#         print(arg1[elements], arg2[elements]) # Use element as arg[index] to reveal arg's values


# def together(arg1, arg2):
#     for index, arg in enumerate(arg1):
#         print(arg, arg2[index])                # Use enumerate to help cycle thru arg. Use index to cycle and print arg2's value


def together(arg1, arg2):                        # Increment thru arg indices using changing counter value in loop
    counter = 0
    while counter < len(arg1):
        print(arg1[counter], arg2[counter])
        counter += 1