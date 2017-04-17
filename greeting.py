
"""

created by Steve Hanlon April 2017

"""

def result(name, age):
    """
    :param name: 
    :param age: 
    :return: a simple program that, 
    when run, prompts the user for their name and age, 
    then prints a greeting and a message about how old they will be a year from now.

    """
    next_year = age + 1
    input(f"Well, {name} that means you'll be {next_year} years old a year from now.")


def questions():
    """
    
    :return: input name and age then pass those as arguments to result(name, age)
    """
    nombre = input("What's your name? ⤏")
    edad = int(input("How old are you? ⤏"))
    result(nombre, edad)

questions()