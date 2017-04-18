"""

>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> display_indexes(a)
m 0
u 1
s 2
i 3
c 4


>>> parallel(a, b)
m 17
u 28
s 42
i 31
c 12

"""

def display_indexes(itty):                   # Using while with incremental counter
    counter = 0
    while counter <= len(itty):
        print(itty[counter], counter)
        counter += 0

#
# def display_indexes(itty):                    # Using enumerate with one arg
#     for index, element in enumerate(itty):    # Use enumerate to add numbers to element values at each index
#         print(element, index)
#

# def parallel(arg1, arg2):                       # Using enumerate with two args
#     for index, element in enumerate(arg1):      # Use enumerate to add numbers and use them to access element values at each index
#         print(element, arg2[index])


# def parallel(arg1, arg2):                       # Using zip with two args
#     for first_in_tuple, sec_in_tuple in zip(arg1, arg2):
#         print(first_in_tuple, sec_in_tuple)


def parallel(arg1, arg2):          # Using while with incremental counter
    counter = 0
    while counter <= len(arg1):
        print(arg1[counter], arg2[counter])
        counter += 1