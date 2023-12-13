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


def part_two(data_list: list):
    sum = 0
    numeric_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }


# def main(do_tests: bool = False):
#     with open("input.txt", "r") as file:
#         lines: list = file.readlines()

#     if do_tests:
#         lines: list = [
#             "two1nine",
#             "eightwothree",
#             "abcone2threexyz",
#             "xtwone3four",
#             "4nineeightseven2",
#             "zoneight234",
#             "7pqrstsixteen",
#         ]

#     numeric_dict = {
#         # "zero": 0,
#         "one": 1,
#         "two": 2,
#         "three": 3,
#         "four": 4,
#         "five": 5,
#         "six": 6,
#         "seven": 7,
#         "eight": 8,
#         "nine": 9,
#         # "0": 0,
#         "1": 1,
#         "2": 2,
#         "3": 3,
#         "4": 4,
#         "5": 5,
#         "6": 6,
#         "7": 7,
#         "8": 8,
#         "9": 9,
#     }

#     def extract_values(line: str) -> int:
#         # Extract first and second digits from the line, return as int
#         line: str = line.lower()  # make Lower case

#         # Find indices
#         number_indices: list = [
#             (line.index(dig), val) for dig, val in numeric_dict.items() if dig in line
#         ]

#         f_dig: int = min(number_indices, key=lambda x: x[0])[1]  # Find smallest index
#         l_dig: int = max(number_indices, key=lambda x: x[0])[1]  # Find largest index

#         result = f_dig * 10 + l_dig
#         return result

#     lines: list = [extract_values(line) for line in lines]
#     total = sum(lines)
#     print(f"Sum is: {total}")


if __name__ == "__main__":
    data = get_data("aoc_day1_input.txt")
    print(f"The sum of all calibration values for part one: {part_one(data)}")
