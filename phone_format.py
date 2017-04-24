"""
Write a small app that asks the user for an all-digits phone number, Then 'pretty prints'

> 503-555-1234

or

> (503) 555-1234

"""

def call_me():
    phone_num = list(input("Yo!  What's up! Please enter your phone number."))

    phone_num.insert(3, '-')
    phone_num.insert(7, '-')

    final = ' '.join(phone_num)
    print(final)

call_me()


def call_me():
    phone_num = list(input("Yo!  What's up! Please enter your phone number."))

    phone_num[0:0] = '('
    phone_num[4:4] = ') '
    phone_num[9:9] = '-'

    final = ''.join(phone_num)
    print(final)

call_me()