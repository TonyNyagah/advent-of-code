def getData(txt_file) -> tuple:
    """Get data from a txt file and return a list of lists."""
    with open(txt_file, "r") as f:
        data = f.read().splitlines()

    # index of the empty space before the instructions start
    empty_string = data.index("")
    # the stacks are located before the empty string
    stack_location = slice(0, empty_string)
    stacks = data[stack_location]
    # we can ignore the last string in the array since it just contains the stack numbers
    stacks = stacks[:-1]
    # select every 4th element in the lists since there are 4 spaces/characters before each letter
    stacks = [letter[1::4] for letter in stacks]
    # turn each string into a list to separate each value including empty values
    stacks = [list(n) for n in stacks]
    # transpose the values so that everything in position 1 of each list is in the same list and so on
    stacks = [list(n) for n in zip(*stacks)]

    instructions = data[empty_string:]
    instructions.remove("")

    instruction_list = []

    for instruction in instructions:
        instruction = instruction.split()
        to_move = int(instruction[1])
        from_stack = int(instruction[3]) - 1
        to_stack = int(instruction[5]) - 1

        instruction_list.append([to_move, from_stack, to_stack])

    return stacks, instruction_list


def moveThings(stacks: list, instructions: list) -> str:
    """Takes in a list of lists and instructions and use the instructions to move around data in the list of lists.
    - 'move 1 from 2 to 1' translates to move one thing from stack 2 to stack 1"""
    pass


def main():
    data = getData("test.txt")
    print(data)


if __name__ == "__main__":
    main()
