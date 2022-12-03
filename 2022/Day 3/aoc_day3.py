def getData(txt_file) -> list:
    """Get data from a text file."""
    with open(txt_file, "r") as f:
        data_list = f.read().splitlines()
    return data_list


def partOne(data: list) -> list:
    """Solves part 1"""
    split_data = []

    for n in data:
        first_compartment = n[: len(n) // 2]
        second_compartment = n[len(n) // 2 :]


def splitDataPart1(data: list) -> list:
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


def countUniqueItemsPartOne(list_of_sets: list) -> int:
    """Count the number of unique items in a list of sets."""
    result = 0

    for n in list_of_sets:
        char = n.pop()
        if char.isupper():
            result += ord(char) - ord("A") + 27
        else:
            result += ord(char) - ord("a") + 1

    return result


def countUniqueItemsPartTwo(list_of_sets: list) -> int:
    """Count the number of unique items in each set of 3 strings."""
    result = 0


def main():
    data = getData("aoc_day3_input.txt")
    split_data = splitDataPart1(data)
    common_items = commonItems(split_data)
    unique_item_count = countUniqueItemsPartOne(common_items)

    print(unique_item_count)


if __name__ == "__main__":
    main()
