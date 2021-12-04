"""
--Part 1 --
forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.

so:
* forward 5 adds 5 to your horizontal position, a total of 5.
* down 5 adds 5 to your depth, resulting in a value of 5.
* forward 8 adds 8 to your horizontal position, a total of 13.
* up 3 decreases your depth by 3, resulting in a value of 2.
* down 8 adds 8 to your depth, resulting in a value of 10.
* forward 2 adds 2 to your horizontal position, a total of 15.

After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)


--Part 2--
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
    It increases your horizontal position by X units.
    It increases your depth by your aim multiplied by X.

so:
* forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
* down 5 adds 5 to your aim, resulting in a value of 5.
* forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
* up 3 decreases your aim by 3, resulting in a value of 2.
* down 8 adds 8 to your aim, resulting in a value of 10.
* forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.

After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)
"""


def get_data_list(file_name):
    with open(file_name) as f:
        input_list = f.read().splitlines()
        return input_list


def loop_over_data_and_sort_directions_and_positions(input_list):
    """
    Loops over the given data list, splits the list into individual pieces of direction and movement points and determines the final horizontal position and depth.

    Args:
        input_list (str): The name of the file containing data to be used.
        aim (boolean, optional): Used to check if aim is taken into account. Defaults to None.
    """
    data_list = get_data_list(input_list)
    horizontal_position = 0
    depth = 0
    for i in data_list:
        individual_split_data_piece = i.split()
        movement_numbers = int(individual_split_data_piece[1])
        if "forward" in individual_split_data_piece:
            horizontal_position += movement_numbers
        elif "up" in individual_split_data_piece:
            depth -= movement_numbers
        elif "down" in individual_split_data_piece:
            depth += movement_numbers

    print("Final horizontal position: {}".format(horizontal_position))
    print("Final depth: {}".format(depth))
    print(
        "The final horizontal position multiplied by the final depth is: {}".format(
            horizontal_position * depth
        )
    )
    print("=======================================================================")


def loop_over_data_and_sort_directions_and_positions_and_aim(input_list):
    data_list = get_data_list(input_list)
    horizontal_position = 0
    depth = 0
    aim = 0
    for i in data_list:
        individual_split_data_piece = i.split()
        direction = individual_split_data_piece[0]
        movement_numbers = int(individual_split_data_piece[1])
        if "forward" in direction:
            horizontal_position += movement_numbers
            aim += movement_numbers * depth
        if "up" in direction:
            depth -= movement_numbers
        if "down" in direction:
            depth += movement_numbers

    print("Final horizontal position: {}".format(horizontal_position))
    print("Final depth: {}".format(depth))
    print("Final aim: {}".format(aim))
    print(
        "The final horizontal position multiplied by the final depth when taking into account aim is: {}".format(
            horizontal_position * aim
        )
    )


def main():
    loop_over_data_and_sort_directions_and_positions("aoc_day2_input.txt")
    loop_over_data_and_sort_directions_and_positions_and_aim("aoc_day2_input.txt")


main()

