import itertools
import re


def get_data(txt_file) -> list:
    with open(txt_file, "r") as f:
        data_list = f.read().splitlines()
    return data_list


def part_one(data_list: list):
    sum = 0

    for n in range(len(data_list)):
        first_digit, last_digit = "", ""
        # print(data_list[n])
        for j in data_list[n]:
            if j.isdigit():
                if first_digit == "":
                    first_digit = j
                last_digit = j

        if first_digit != "" and last_digit != "":
            calibration_value = int(first_digit + last_digit)
            sum += calibration_value

    return sum


if __name__ == "__main__":
    data = get_data("aoc_day1_input.txt")
    print(f"The sum of all calibration values is: {part_one(data)}")
