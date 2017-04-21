"""

>>> validate([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])
Valid!

>>> validate([6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4])
Invalid!

"""


def validate(account_number):
   """
   1. Slice off the last digit.  That is the **check digit**.
   2. Reverse the digits.
   3. Double every other element in the reversed list.
   4. Subtract nine from numbers over nine.
   5. Sum all values.
   6. Take the second digit of that sum.
   7. If that matches the check digit, the whole card number is valid.
   :param account_number: 
   :return: boolean 
   """

"""
refactored
"""


def validate(account_number):
   # Write your code here.

   check_digit = account_number.pop()
   account_number.reverse()

   for index, number in enumerate(account_number):
      if index % 2 == 0:
         refract = number * 2
         if refract > 9:
            refract -= 9
      else:
         refract = number

   second_digit = int(str(sum(account_number))[1])

   if second_digit == check_digit:
      print('Valid!')
   else:
      print('Invalid!')


validate([6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4])



#
# """
# first incarnation
# """
#
# check_digit = account_number.pop()
#
# account_number.reverse()
#
# for index, number in enumerate(account_number):
#    if index % 2 == 0:
#       refract = account_number[index] * 2
#       if refract > 9:
#          refract -= 9
#    else:
#       refract = account_number[index]
#
# grand_sum = str(sum(account_number))
#
# sliced_digit = grand_sum[1:]
#
# if int(sliced_digit) == check_digit:
#    print('Valid!')
# else:
#    print('Invalid!')