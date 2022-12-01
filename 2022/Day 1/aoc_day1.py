from more_itertools import split_at


def getData(txt_file) -> list:
    """Get data from a text file and remove new line characters."""
    with open(txt_file, "r") as f:
        data_list = f.read().splitlines()
    return data_list


def mergeData(data_list) -> list:
    """Create a list of lists by removing empty strings."""
    list_of_lists = list(split_at(data_list, lambda x: x == ""))
    list_of_lists = [[int(j) for j in i] for i in list_of_lists]
    return list_of_lists


def listSums(list_of_lists) -> list:
    """Add up the value of each individual list."""
    list_of_sums = [sum(l) for l in list_of_lists]
    return list_of_sums


def largestNumber(list_of_sums):
    """Return the largest number in the list."""
    return max(list_of_sums)


def sortList(list_of_sums):
    """Sort the list of sums."""
    return sorted(list_of_sums)


def topThreeSum(sorted_list):
    """Sum up the three largest values in the list.
    - Since the list is sorted from smallest to largest, we sum up the three numbers at the bottom of the list.
    """
    return sum(sorted_list[-3::])


if __name__ == "__main__":
    data = getData("aoc_day1_input.txt")
    data_lists = mergeData(data)
    list_sums = listSums(data_lists)

    sorted_list = sortList(list_sums)

    largest_amount = largestNumber(list_sums)
    sum_of_largest_values = topThreeSum(sorted_list)

    print(f"Largest amount carried: {largest_amount}")
    print(f"Sum of largest values: {sum_of_largest_values}")
