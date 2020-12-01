"""Advent of Code 2020 Day 1: Report Repair"""

"""What is the product of the three entries that sum to 2020?"""




from functools import reduce
def get_and_sort(file):
    data = []
    f = open(file, "r")

    for n in f:
        data.append(int(n))

    return sorted(data)


def brute_force(file):
    data = get_and_sort("input.txt")
    final_data = []

    for i in sorted(data):
        for j in sorted(data):
            for n in sorted(data):
                if i + j + n == 2020:
                    final_data.append(i)
                    final_data.append(j)
                    final_data.append(n)

    # remove duplicates from the final data
    no_duplicates_data = list(set(final_data))
    # multiply all numbers in the list
    print(reduce(lambda x, y: x*y, no_duplicates_data))


brute_force("input.txt")
