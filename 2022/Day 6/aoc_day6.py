def getData(txt_file) -> list:
    """Get a string from a text file."""
    with open(txt_file, "r") as f:
        data = f.read()

    return data


def sliding_window(string: str, window_size: int):

    for i in range(len(string) - window_size + 1):
        current_window = string[i : i + window_size]
        if len(set(current_window)) == len(current_window):
            # print(current_window)
            return i + window_size


def main():
    data = getData("aoc_day6_input.txt")

    print
    print(f"Part 1: {sliding_window(data, 4)}")
    print(f"Part 2: {sliding_window(data, 14)}")


if __name__ == "__main__":
    main()
