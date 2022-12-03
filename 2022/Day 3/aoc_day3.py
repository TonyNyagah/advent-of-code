# import re


# def main():
#     with open("input.txt") as f:
#         lines = f.readlines()

#     # Part 1
#     print(sum(find_priority(line) for line in lines))

#     # Part 2
#     print(sum(find_common_letters(line) for line in lines))


# def find_priority(line):
#     """
#     Find the priority of the item type that appears in both compartments of the rucksack.
#     """
#     first_compartment = line[: len(line) // 2]
#     second_compartment = line[len(line) // 2 :]
#     common_letters = set(first_compartment) & set(second_compartment)
#     return min(ord(letter) - 96 for letter in common_letters)


# def find_common_letters(line):
#     """
#     Find the common letters between the two compartments of the rucksack.
#     """
#     first_compartment = line[: len(line) // 2]
#     second_compartment = line[len(line) // 2 :]
#     common_letters = set(first_compartment) & set(second_compartment)
#     return sum(ord(letter) - 96 for letter in common_letters)


# if __name__ == "__main__":
#     main()


def getData(txt_file) -> list:
    """Get data from a text file."""
    with open(txt_file, "r") as f:
        data_list = f.read().splitlines()
    return data_list


def splitData(data: list) -> list:
    """Split each value in the received data into two separate values."""
    split_data = []

    for n in data:
        first_compartment = n[: len(n) // 2]
        second_compartment = n[len(n) // 2 :]
        split_data.append([first_compartment, second_compartment])

    return split_data


def commonItems(data: list) -> list:
    """Looks for common items in each list of lists received by the function."""
    common_items = []

    for n in data:
        common_items.append(set(n[0]).intersection(n[1]))

    return common_items


def countUniqueItems(list_of_sets: list) -> int:
    result = 0

    for n in list_of_sets:
        char = n.pop()
        if char.isupper():
            result += ord(char) - ord("A") + 27
        else:
            result += ord(char) - ord("a") + 1

    return result


def main():
    data = getData("aoc_day3_input.txt")
    split_data = splitData(data)
    common_items = commonItems(split_data)
    unique_item_count = countUniqueItems(common_items)

    print(unique_item_count)


if __name__ == "__main__":
    main()
