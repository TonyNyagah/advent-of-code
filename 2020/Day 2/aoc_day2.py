"""--- Day 2: Password Philosophy ---"""


def password_checker_1(data):
    """
    Accepts an array that holds passwords to be checked against a specific criteria.

    Args:
        data (array): holds various strings of characters that are used to validate a password

    Check that the password contains a minimum of the first number and a maximum
    of the second number of the given character i.e.
    in '1-3 a: abcde', the password 'abcde' should have a minimum of 1 a and a maximum of 3 a's
    """
    valid = 0
    input_split = ""
    occurence = ""
    lowest_occurence = ""
    highest_occurence = ""
    desired_char = ""

    # split the data
    for n in data:
        input_split = n.split()

        occurence = input_split[0].split("-")

        lowest_occurence = int(occurence[0])
        highest_occurence = int(occurence[-1])

        desired_char = input_split[1][:-1]

        password = input_split[-1]

        if password.count(desired_char) >= lowest_occurence and password.count(desired_char) <= highest_occurence:
            valid += 1

    # print(input_split)
    # print(occurence)
    # print(lowest_occurence)
    # print(highest_occurence)
    # print(desired_char)
    # print(password)
    print("Valid passwords according to password rule 1: {}.".format(valid))


def password_checker_2(data):
    """
    Accepts an array that holds passwords to be checked against a specific criteria.

    Args:
        data (array): holds various strings of characters that are used to validate a password

    Check that the password contains given characters in specific positions i.e.
    in '1-3 a: abcde', the password 'abcde' should have a in position 1 or 3 but not in both positions
    """
    valid = 0
    input_split = ""
    indexes = ""
    lower_index = ""
    higher_index = ""
    desired_char = ""

    # split the data
    for n in data:
        input_split = n.split()

        indexes = input_split[0].split("-")

        lower_index = int(indexes[0])
        higher_index = int(indexes[-1])

        desired_char = input_split[1][:-1]

        password = input_split[-1]

        if password[lower_index - 1] == desired_char and password[higher_index - 1] != desired_char:
            valid += 1
        elif password[lower_index - 1] != desired_char and password[higher_index - 1] == desired_char:
            valid += 1

    # print(input_split)
    # print(indexes)
    # print(lower_index)
    # print(higher_index)
    # print(desired_char)
    # print(password)

    print("Valid passwords according to password rule 2: {}.".format(valid))


def main():
    # read from the input file
    data = []
    f = open("input.txt", "r")
    for n in f:
        data.append(n)

    # send the sorted data to the password checker functions
    password_checker_1(data)
    password_checker_2(data)


if __name__ == "__main__":
    main()
