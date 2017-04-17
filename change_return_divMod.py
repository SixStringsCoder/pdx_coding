"""
Something Something
"""


def change_dispenser():
    change_back = float(input("Enter a change amount under one dollar. >> "))
    while True:
        quarters, change_left = divmod(change_back, .25) # Quantity of quarters in change_back
        dimes, change_left = divmod(change_left, .1) # Quantity of dimes in change_back
        nickels, change_left = divmod(change_left, .05) # Quantity of nickels in change_back
        pennies, change_left = divmod(change_left, .01) # Quantity of pennies in change_back
        print(f"""
        Your change is divided into 
        {quarters} quarters,
        {dimes} dimes,
        {nickels} nickels, and
        {pennies} pennies.
        """)
        break

change_dispenser()