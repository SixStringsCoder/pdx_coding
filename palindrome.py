"""
Write a function that returns True if the input is a palindrome, or False, if it is not.

>>> palindrome('hannah')
True

>>> palindrome('racecar')
True

>>> palindrome('a man, a plan, a canal, Panama')
True

>>> palindrome("1 pound coconut.")
False

>>> palindrome(1234321)
True

"""
def palindrome(test):
    forward = str(test).lower().replace(",", "").replace(" ", "")
    backward = forward[::-1]

    if forward == backward:
        result = True
    else:
        result = False

    return result