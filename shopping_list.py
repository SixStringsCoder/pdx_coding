

# make a list to hold onto our items
shopping_list = []


# have a HELP menu plus first Question to break the ice
def show_help():
    print("What, pray tell, must you have?")
    print("""
-----------MENU-------------    
Type 'done' to quit the app.
Type 'help' to view this menu.
Type 'show' to see the shopping list.
Type 'remove' to remove an item from the list.
""")


# SHOW/PREVIEW the list
def show_list():
    if len(shopping_list) == 0:
        print("Your shopping list is empty.\nAdd items below.")
    else:
        print("Here's your shopping list.")
        for item in shopping_list:
            print(item)


# ADD to the list
def add_to_list(new_thing):
    shopping_list.append(new_thing)
    print("'{}' added to list. You have {} things on your list.".format(new_thing.upper(), len(shopping_list)))


# REMOVE from the list
def remove_item():
    take_away = input("Type item to be exterminated? ")
    try:
        shopping_list.remove(take_away)
    except ValueError:
        print("Oopsy! {} is not on the list.".format(take_away.upper()))
    else:
        print("'{}' exterminated!".format(take_away.upper()))
    show_list()


# start with showing help menu
show_help()


# WHILE loop
while True:
    # ask for new items
    new_item = input("> ")
    # be able to quit he app/help/show/remove
    if new_item.lower() == 'done':
        break
    elif new_item.lower() == 'help':
        show_help()
        continue
    elif new_item.lower() == 'show':
        show_list()
        continue
    elif new_item.lower() == 'remove':
        remove_item()
        continue
    add_to_list(new_item)

# show the list
show_list()
