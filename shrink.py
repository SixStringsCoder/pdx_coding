"""

>>> shrink('1235')
2

>>> shrink('13')
4

>>> shrink('1123581321')
9

"""

def shrink(string_sum):
    """
    write a function to sum all numbers in a string until output is just 
    one digit in length.

    :return: integer
    """
    listify = list(string_sum)
    #  print(listify)
    nother_list = list()

    for i in listify:
        numberfy = int(i)
        nother_list.append(numberfy)
        added = sum(nother_list)
    #  print(added)

    if added < 10:
        print(added)
    #  print(added)

    elif added >= 10:
        string_sum2 = str(added)
        shrink(string_sum2)
