def get_raw_txt_data():
    # open the file containing the list of numbers
    with open("aoc_day1_input.txt", "r") as f:
        # read the numbers from the file, line by line
        data = f.readlines()
        # create a list to store the numbers
        data = [int(x.strip()) for x in data]
    return data


def CumulativeDepthIncrease(data: list):
    """
    This function takes a list as input, reads the numbers given and determines whether the next number is larger than the former.
    The number of times that the next number is larger than the former will be returned as the result.

    Args:
        data (list): a list of numbers
    """

    # loop over the data checking if the next number is larger than the former
    depth_increase_counter = 0
    for i in range(0, len(data) - 1):
        # if the next number is larger than the former, increase the depth_increase-counter
        if data[i + 1] > data[i]:
            depth_increase_counter += 1

    # print(depth_increase_counter)
    return depth_increase_counter


def CumulativeDepthIncreaseInThrees(data: list):
    """
    This function takes the given depth data, loops over said data and adds the current depth to the next two depths given. 
    A list with these sums is returned.

    Args:
        data (list): a list of numbers
    """
    # an array to store the sums of the current number and the next two numbers
    three_sums_array = []
    # loop over the data adding the next 2 numbers to the current one
    # leave out the final 2 numbers to prevent out of range errors
    for i in range(0, len(data) - 2):
        # start at the current number and add the next 2 numbers
        current_three_sum = data[i] + data[i + 1] + data[i + 2]
        # append the sum of the 3 values to the array
        three_sums_array.append(current_three_sum)

    # pass the generated array to the cumulative depth increase function
    return CumulativeDepthIncrease(data=three_sums_array)


print(
    "The result for part 1 is: {}".format(
        CumulativeDepthIncrease(data=get_raw_txt_data())
    )
)
print(
    "The result for part 2 is: {}".format(
        CumulativeDepthIncreaseInThrees(data=get_raw_txt_data())
    )
)
# SonarSweep2()
