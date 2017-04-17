"""
created on Python by SixSringsCoder
Some other comment that meets PEP8 standards
"""

def miles_feet_calc(miles):
    """
    This function holds tons of potential to free the animals in Zanzibar.
    It also passes an argument 'miles' multiplied by feet which then gets formatted into
    a print function
    """
    feet = 5280

    qtyFeet = miles * feet # Prints equal number of feet

    print(f"""{miles} mile(s) equals {qtyFeet} feet.""") # Answer sentence


storage = int(input("How many miles do you want to convert? >>> ")) # Prompt user for number of miles
miles_feet_calc(storage)