"""
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

--PART 1--
Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.
The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.
The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.
So, the gamma rate is the binary number 10110, or 22 in decimal.
The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used.
So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

--PART 2--
Not even gonna bother deciphering that here
"""
from collections import Counter


def get_data_list(file_name: str):
    with open(file_name) as f:
        original_data = f.read().splitlines()
        get_gamma_and_epsilon_rating(original_data)
        get_oxygen_generator_and_co2_scrubber_rating(original_data)


def get_gamma_and_epsilon_rating(data: list):
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(len(data[0])):
        common = Counter([x[i] for x in data])
        if common["0"] > common["1"]:
            gamma_rate += "0"
            epsilon_rate += "1"
        if common["1"] > common["0"]:
            epsilon_rate += "0"
            gamma_rate += "1"
    # convert the strings into int then binary(base 2)
    print("Gamma rate: {}".format(gamma_rate))
    print("Epsilon rate: {}".format(epsilon_rate))
    print(
        "Part 1 gamma rate * epsilon rate in decimal is: {}.".format(
            int(gamma_rate, 2) * int(epsilon_rate, 2)
        )
    )
    print("=====================================================")


def get_oxygen_generator_and_co2_scrubber_rating(data: list):
    oxygen_data = data
    co2_data = data
    oxygen_generator_rating = ""
    co2_scrubber_rating = ""
    for i in range(len(oxygen_data[0])):
        common = Counter([x[i] for x in oxygen_data])
        if common["0"] > common["1"]:
            oxygen_data = [x for x in oxygen_data if x[i] == "0"]
        else:
            oxygen_data = [x for x in oxygen_data if x[i] == "1"]
        oxygen_generator_rating = oxygen_data[0]

    for i in range(len(co2_data[0])):
        common = Counter([x[i] for x in co2_data])
        if common["0"] > common["1"]:
            co2_data = [x for x in co2_data if x[i] == "1"]
        else:
            co2_data = [x for x in co2_data if x[i] == "0"]
        if co2_data:
            co2_scrubber_rating = co2_data[0]

    print("Oxygen generator rating: {}.".format(oxygen_generator_rating))
    print("CO2 scrubber rating: {}.".format(co2_scrubber_rating))
    print(
        "Part 2 oxygen generator rating * CO2 scrubber rating in decimal: {}.".format(
            int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
        )
    )


def main():
    get_data_list("aoc_day3_input.txt")


main()
