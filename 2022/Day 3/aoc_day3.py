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
    first_compartment, second_compartment = (
        data[: len(data) // 2],
        data[len(data) // 2 :],
    )
    split_data = []

    for n in data:
        pass

    pass


def main():
    data = getData("test.txt")

    print(data)
    print([len(x) for x in data])


if __name__ == "__main__":
    main()
