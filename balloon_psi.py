"""
BALLOON PSI TESTER
Make a function to test whether a balloon is full enough or not.
"""



"""
>>> inflator([1, 5, 6, 2, 6, 7], 200)
False

>>> inflator([1,5,6,2,6,7], 500)
False

>>> inflator([1,5,6,2,6,7,20,45,20,23], 1500)
False

>>> inflator([1,5,6,2,6,7,20,45,20,23], 10000)
True

>>> inflator([1,5,6,2,6,7], 2000)
True

>>> inflator([1,5,6,2,6,7], 3000)
False


>>> inflator2([1,5,6,2,6,7,20,45,20,23], 10000, 50)
True

>>> inflator2([1,5,6,2,6,7], 2000, 25)
False

>>> inflator2([1,5,16,2,6,27], 3000, 75)
False

>>> inflator2([1,5,1,2,6,4], 300, 8)
True

"""


def inflator(seconds: list, size: int) -> bool:
    """
    measure the amount of air put in a balloon and determine if the balloon is full enough or not

    :return: boolean
    """
    total_psi = sum(seconds) * 42

    if  total_psi <= int(size / 2) or total_psi > size:  # balloon size under filled or overfilled
        return False
    else:
        return True                                      # balloon is full enough



def inflator2(seconds: list, size: int, psi: int) -> bool:
    """
        measure the amount of air put in a balloon and determine if the balloon 
        is full enough or not.  Use three parameters (adding PSI in this example) for this example.

        :return: boolean
    """
    total_psi = sum(seconds) * psi

    if  total_psi <= int(size / 2) or total_psi > size:  # balloon size under-filled or overfilled and pops
        return False
    else:
        return True                                      # balloon is full enough