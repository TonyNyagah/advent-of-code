"""Advent of Code 2020 Day 1: Report Repair"""

"""Find the two entries that sum to 2020; what do you get if you multiply them together?"""




from functools import reduce
def get_and_sort(file):
    data = []
    f = open(file, "r")

    for n in f:
        data.append(int(n))

    return sorted(data)


def brute_force(file):
    data = get_and_sort(file)
    final_data = []

    for i in sorted(data):
        for j in sorted(data):
            if i + j == 2020:
                final_data.append(i)
                final_data.append(j)

    print("Pair found: {} and {}".format(final_data[0], final_data[1]))
    # remove duplicates from the final data
    no_duplicates_data = list(set(final_data))
    # multiply all numbers in the list
    print(reduce(lambda x, y: x*y, no_duplicates_data))


def binary_search(file, sum):
    data = get_and_sort(file)

    low = 0
    high = len(data) - 1

    while low <= high:
        if data[low] + data[high] == sum:
            print("Pair found: {} and {}.".format(data[low], data[high]))
            print(data[low] * data[high])
            return
        if data[low] + data[high] < sum:
            low = low + 1
        else:
            high = high - 1


brute_force("input.txt")
binary_search("input.txt", 2020)
