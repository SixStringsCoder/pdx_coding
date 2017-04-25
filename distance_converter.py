"""
next refactor ---> make function to start off prompts...
lead to function for straight-forward conversions and 2nd function for
2-step conversions
"""

import math

def converter():
    # meter = 1
    # feet = 3.28084
    # kilom = 1000
    # mile = 1609.344

    # # Make one print statement here with variable and print just that
    # result = f"{distance} {start_unit} is {conversion} {target_unit}"

    distance = input("Enter a distance: ")
    start_unit = input("Enter units (mi, km, ft or m): ")
    target_unit = input("Enter target units (mi, km, ft or m): ")

    if start_unit == 'mi' and target_unit == 'ft':  # mi to ft
        conversion = int(distance) * 5280
        print(f"There are {conversion} feet in {distance} mile(s).")

    elif start_unit == 'ft' and target_unit == 'mi':  # ft to mi
        conversion = int(distance) / 5280
        print(f"There are {conversion} mile(s) in {distance} feet.")

    elif start_unit == 'km' and target_unit == 'm':  # km to m
        conversion = int(distance) * 1000
        print(f"There are {conversion} meter(s) in {distance} kilometers.")

    elif start_unit == 'm' and target_unit == 'km':  # m to km
        conversion = int(distance) / 1000
        print(f"There are {conversion} kilometers(s) in {distance} meters.")

    elif start_unit == 'm' and target_unit == 'ft':  # m to ft
        conversion = int(distance) * 3.28084
        print(f"There are {math.ceil(conversion)} feet in {distance} meters.")

    elif start_unit == 'm' and target_unit == 'mi':   # m to mi
        conversion = int(distance) * 3.28084 / 5280
        print(f"There are {math.ceil(conversion)} miles in {distance} meters.")

    elif start_unit == 'km' and target_unit == 'mi':   # km to mi
        conversion = int(distance) * 1000 * 3.28084 / 5280
        print(f"There are {round(conversion, 2)} miles in {distance} kilometers.")

    elif start_unit == 'km' and target_unit == 'ft':   # km to ft
        conversion = int(distance) * 1000 * 3.28084
        print(f"There are {math.ceil(conversion)} miles in {distance} kilometers.")

    elif start_unit == 'ft' and target_unit == 'm':  # ft to m
        conversion = int(distance) / 3.28084
        print(f"There are {math.ceil(conversion)} meters in {distance} feet.")

    elif start_unit == 'ft' and target_unit == 'km':  # ft to km
        conversion = int(distance) / 3.28084 / 1000
        print(f"There are {math.ceil(conversion)} kilometers in {distance} feet.")

    elif start_unit == 'mi' and target_unit == 'm':  # mi to m
        conversion = int(distance) / 1609.344
        print(f"There are {round(conversion, 2)} meters in {distance} miles.")

    elif start_unit == 'mi' and target_unit == 'km':  # mi to km
        conversion = int(distance) / 1609.344 / 1000
        print(f"There are {math.ceil(conversion)} kilometers in {distance} miles.")

    else:
        print(f"That input isn't valid. Try again.")
        converter()


converter()
