def getData(txt_file) -> list:
    """Get data from a text file."""
    data_list = []

    with open(txt_file, "r") as f:
        data = f.read().splitlines()
        for i in data:
            i = i.split(",")
            i[0] = list(map(int, i[0].split("-")))
            i[1] = list(map(int, i[1].split("-")))
            data_list.append([i[0], i[1]])

    return data_list


def compareData(data_list: list) -> int:
    """Takes in a list of list and checks if the ranges of data in those lists are in each other.
    * Returns an int showing how many of the lists are subsets of each other.
    * Returns a second int showing how much of the data overlaps."""
    subsets = 0
    overlaps = 0

    for ls in data_list:
        # [*range(ls[0][0], ls[0][1] + 1)]
        list1 = [*range(ls[0][0], ls[0][1] + 1)]
        list2 = [*range(ls[1][0], ls[1][1] + 1)]

        if set(list1).issubset(list2) or set(list2).issubset(list1):
            subsets += 1
        if set(list1).intersection(set(list2)) or set(list2).intersection(set(list1)):
            overlaps += 1

    return f"Number of subsets: {subsets}", f"Number of overlaps: {overlaps}"


def main():
    data = getData("aoc_day4_input.txt")
    compare_data = compareData(data)

    print(compare_data)


if __name__ == "__main__":
    main()
