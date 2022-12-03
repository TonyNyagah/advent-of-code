def getData(txt_file) -> list:
    """Get data from a text file."""
    with open(txt_file, "r") as f:
        data_list = f.read().splitlines()
    return data_list


def partOne(data: list) -> list:
    """Solves part 1"""
    result = 0

    for n in data:
        first_compartment = n[: len(n) // 2]
        second_compartment = n[len(n) // 2 :]

        for char in set(first_compartment):
            if char in second_compartment:
                result += ord(char) - ord("A") + 27
            else:
                result += ord(char) - ord("a") + 1
            break

    return result


def main():
    data = getData("aoc_day3_input.txt")
    part_one_result = partOne(data)

    print(f"Part 1 answer: {part_one_result}")


if __name__ == "__main__":
    main()
