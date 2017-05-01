import chalk


def stop(phonebook):
    chalk.green("Take it easy, mon.  Rasta forever! ☯")             # Quit phone book
    quit()


def find(request, phonebook):                                      # Find a person
    # request.replace('-', '')  # use if phone number query included

    for index, entry in enumerate(phonebook):
        if request in entry['First Name']:
            print(entry)
            break
    else:                                               # only happens if name is not found
        chalk.red("Not in phone book.  Sorry.")


def take_away(phonebook):                                           # Remove a person
    banish = input("Enter the name of person to remove from phone book. >> ")

    for index, entry in enumerate(phonebook):
        if banish in entry['First Name']:
            del phonebook[index]
    chalk.red(f"{banish} has been removed form your phonebook forever!")


def query(phonebook):
    request = input("Enter name to find. >> ")
    find(request, phonebook)


def view(phonebook):                                                # View whole phone book
    """
    >>> phonebook = [{'First Name': 'Grover', 'Last Name': 'Washington', 'Phone': '234-9876'}, {'First Name': 'Billie', 'Last Name': 'Holiday', 'Phone': '451-2861'}, {'First Name': 'Joe', 'Last Name': 'Pass', 'Phone': '498-1234'}]

    >>> view(phonebook)
    [{'First Name': 'Grover', 'Last Name': 'Washington', 'Phone': '234-9876'}, {'First Name': 'Billie', 'Last Name': 'Holiday', 'Phone': '451-2861'}, {'First Name': 'Joe', 'Last Name': 'Pass', 'Phone': '498-1234'}]

    """

    if len(phonebook) == 0:
        chalk.red("Your phone book is empty.")
    else:
        print(phonebook)


def add(phonebook):                                                 # Add to phonebook
    """
    {'name': 'Kieran', 'number': 8456331959, 'phrase': 'Good code is not written, it\'s re-written.'}
    :return: dictionary user entry, added to larger phone book list
    """
    person_entry = dict()

    user = input("Enter first name. >> ")
    last = input("Enter last name? >> ")
    phone = input("Enter phone number? >> ")

    person_entry.update({'First Name': user.capitalize(), 'Last Name': last.capitalize(), 'Phone': phone})
    phonebook.append(person_entry)
    chalk.yellow(f"{user} has been added to the phone book.")


def menu():
    chalk.cyan("""
    -----------MENU-------------    
    Type 'help' to view this menu.
    -----------------------------
    Type 'view' ------> view phonebook.
    Type 'add' -------> add a person.
    Type 'find' ------> find a person.
    Type 'remove' ----> remove a person.
    Type 'quit' ------> quit the phonebook.
    """)


def start():                                        # Engine with dictionaries values being functions

    options = {'help': menu,
               'view': view,
               'add': add,
               'find': query,
               'remove': take_away,
               'quit': stop }

    phonebook = list()
    menu()

    while True:
        ask = input("What do you want to do? >> ").lower()

        try:
            options[ask](phonebook)
        except KeyError:
            chalk.red('Bad input. Try again')
        except TypeError:
            menu()


if __name__ == "__main__":

    start()
