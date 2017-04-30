trees = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics', 'SQL'],
         'Kenneth Love': ['Python Basics', 'Python Collections']}


def num_teachers(trees: dict): -> int
    """
    The num_teachers function should return an integer for how many teachers are in the dict.
    """

    how_many = [key for key in trees.keys()]

    print(len(how_many))

num_teachers(trees)


def courses(trees: dict): -> list
    """
    combine course lists in the dict.
    """

    new_list = list()

    for course in trees.values():
        new_list.extend(course)
    return new_list

courses(trees)


def most_courses(treehouse): -> string
    """
    return the name of the teacher who is teaching the most courses
    """

    most = max([len(item[1]) for item in treehouse.items()])

    for teacher in treehouse.items():
        if len(teacher[1]) == most:
            return (teacher[0])

most_courses(trees)


def stats(trees): -> list
    """
    return two sublists within a list of teachers' names and courses taught 
    """
    result = [[item[0], len(item[1])] for item in trees.items()]
    return result


stats(trees)