"""
This Python file created by SixStringsCoder.
A module that demonstrates the usage of returning the gallons 
of paint needed to paint one unique wall.
"""


def wall_painting(width, height, cost, coats):
    """Figure out then print how much it will cost to paint the wall with one coat."""

    total_gallons = 0
    total_cost = 0

    while True:
        area = width * height
        total_gallons += int((float(area / 400) * coats))
        total_cost += int((total_gallons * cost))
        print(f"So far you'll need to buy {total_gallons} gallons and it will cost you ${total_cost}.")

        more_walls = input("Do you have another wall to paint? Y/n ")
        if more_walls.lower() != 'n':
            gather_info()
        else:
            print(f"In total you'll need to buy {total_gallons} gallons and it will cost you ${total_cost}.")
            quit()

    print(f"In total you'll need to buy {total_gallons} gallons and it will cost you ${total_cost}.")


def gather_info():
    """These are prompts to gather the arguments to pass in wall_painting function"""
    width_of_wall = int(input("What is the width of your wall in feet? >> "))  # What is width of the wall
    height_of_wall = int(input("What is the height of your wallin feet? >> "))  # What is height of the wall
    cost_per_gallon = float(input("How much does a gallon of paint cost? >> "))  # How much a gallon of paint costs
    coats_of_paint = int(input("How many coats will you put on? >> ")) # How many coats of paint
    # sys.exit()
    wall_painting(width_of_wall, height_of_wall, cost_per_gallon, coats_of_paint)


gather_info()