"""

>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

>>> peaks(data)
[6, 14]

>>> valleys(data)
[9, 17]

>>> peaks_and_valleys(data)
[6, 9, 14, 17]

>>> points_of_interest = peaks_and_valleys(data)

>>> chop(data, points_of_interest)
[[1, 2, 3, 4, 5, 6, 7], [6, 5, 4], [5, 6, 7, 8, 9], [8, 7, 6], [7, 8, 9]]

"""


def peaks(it):
    peak_indices = list()

    for i, elem in enumerate(it):
        if i == 0 or i == len(it) - 1:
            continue

        this_one = it[i]
        next_one = it[i + 1]
        prev_one = it[i - 1]

        if this_one > prev_one and this_one > next_one:
            peak_indices.append(i)

    return peak_indices


def valleys(it):
    valley_indices = list()

    for i, elem in enumerate(it):
         if i == 0 or i == len(it) - 1:
             continue

         this_one = it[i]
         next_one = it[i + 1]
         prev_one = it[i - 1]

         if this_one < prev_one and this_one < next_one:
             valley_indices.append(i)

    return valley_indices


# def peaks_and_valleys(it):
#     p_v_indices = list()
#
#     for i, elem in enumerate(it):
#         if i == 0 or i == len(it) - 1:
#             continue
#
#         this_one = it[i]
#         next_one = it[i + 1]
#         prev_one = it[i - 1]
#
#         if prev_one == next_one:
#             p_v_indices.append(i)
#
#     print(p_v_indices)


def peaks_and_valleys(it):

    peak_list = peaks(it)
    valley_list = valleys(it)

    return sorted(peak_list + valley_list)


# def chop(it, slope_pts):
#     chop_list = list()
#
#     slope_points = peaks_and_valleys(it)
#
#     for i, point in enumerate(slope_points):
#
#         try:
#             this_one, next_one = point, slope_points[i+1]
#         except IndexError:
#             print(chop_list)
#
#
#         sub_list = it[:this_one + 1]
#         chop_list.append(sub_list)




