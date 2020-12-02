"""Advent of Code 2020 Day 1: Report Repair"""

"""1. Find the two entries that sum to 2020; what do you get if you multiply them together?"""
"""2. What is the product of the three entries that sum to 2020?"""


def findPairs(data, sum):
    low_end = 0
    high_end = len(data) - 1

    while low_end <= high_end:
        if data[low_end] + data[high_end] == sum:
            print("Pair with given sum is {} and {}.".format(
                data[low_end], data[high_end]))
            print("Multiplying them gives us: {}.".format(
                data[low_end] * data[high_end]))
            print("=================================================================")
            return
        elif data[low_end] + data[high_end] < sum:
            low_end = low_end + 1
        else:
            high_end = high_end - 1


def findTrio(data, sum):
    arr_size = len(data)

    for i in range(0, arr_size-2):
        low_end = i + 1
        high_end = arr_size - 1
        while low_end <= high_end:
            if data[i] + data[low_end] + data[high_end] == sum:
                print("Pair with given sum is {}, {} and {}.".format(
                    data[i], data[low_end], data[high_end]))
                print("Multiplying them gives us: {}.".format(
                    data[i] * data[low_end] * data[high_end]))
                print(
                    "=================================================================")
                return
            elif data[i] + data[low_end] + data[high_end] < sum:
                low_end = low_end + 1
            else:
                high_end = high_end - 1


def main():
    # read from the input file and save the input data in an array
    # sort said data too
    data = []
    f = open("input.txt", "r")
    for n in f:
        data.append(int(n))
    sorted_data = sorted(data)

    # send the sorted data to the search functions
    findPairs(sorted_data, 2020)
    findTrio(sorted_data, 2020)


if __name__ == "__main__":
    main()
