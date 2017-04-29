"""

>>> quantify_words("Red touching black is a friend of Jack, Red touching yellow can kill a fellow.")
a 2
black 1
can 1
fellow 1
friend 1
is 1
jack 1
kill 1
of 1
red 2
touching 2
yellow 1


>>> quantify_words("In the end, it's concluded that the airspeed velocity of a \
(European) unladen swallow is about 24 miles per hour or 11 meters per second.")
(european) 1
11 1
24 1
a 1
about 1
airspeed 1
concluded 1
end 1
hour 1
in 1
is 1
it's 1
meters 1
miles 1
of 1
or 1
per 2
second 1
swallow 1
that 1
the 2
unladen 1
velocity 1
"""


def quantify_words(multi_lined_string):
    """
    Write a function that quantifies how many times a word occurs in a given string.
    :param multi_lined_string:
    :return:
    """
    str_to_list = multi_lined_string.replace('.', '').replace(',', '').lower().split()
    list_sort = sorted(str_to_list)

    for word in list_sort:
        count_occ = list_sort.count(word)
        if list_sort.count(word) > 1:
            list_sort.remove(word)

        print(word, count_occ)