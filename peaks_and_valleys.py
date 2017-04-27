"""

>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

>>> peaks(data)
[6, 14]

# >>> valleys(data)
# [9, 17]
# 
# >>> peaks_and_valleys(data)
# [6, 9, 14, 17]
# 
# >>> points_of_interest = peaks_and_valleys(data)
# 
# >>> chop(data, points_of_interest)
# [[1, 2, 3, 4, 5, 6, 7], [6, 5, 4], [5, 6, 7, 8, 9], [8, 7, 6], [7, 8, 9]]

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


