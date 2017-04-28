"""

>>> 
>>> fibo(10)
[1, 1, 2, 3, 5, 8]

>>> fibo(20)
[1, 1, 2, 3, 5, 8, 13]

>>> fibo(30)
[1, 1, 2, 3, 5, 8, 13, 21]

"""


def fibo(ceil_value):
    a, b = 0, 1
    fibo_list = list()

    while b < ceil_value:
        a, b = b, a + b
        fibo_list.append(a)
    return fibo_list