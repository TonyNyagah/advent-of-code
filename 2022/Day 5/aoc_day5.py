# def getData(txt_file) -> tuple:
#     """Get data from a txt file and return a list of lists."""
#     with open(txt_file, "r") as f:
#         data = f.read().splitlines()

#     # index of the empty space before the instructions start
#     empty_string = data.index("")
#     # the stacks are located before the empty string
#     stack_location = slice(0, empty_string)
#     stacks = data[stack_location]
#     # we can ignore the last string in the array since it just contains the stack numbers
#     stacks = stacks[:-1]
#     # select every 4th element in the lists since there are 4 spaces/characters before each letter
#     stacks = [letter[1::4] for letter in stacks]
#     # turn each string into a list to separate each value including empty values
#     stacks = [list(n) for n in stacks]
#     # transpose the values so that everything in position 1 of each list is in the same list and so on
#     stacks = [list(n) for n in zip(*stacks)]

#     stacks = [[x for x in sublist if x != " "] for sublist in stacks]

#     instructions = data[empty_string:]
#     instructions.remove("")

#     instruction_list = []

#     for instruction in instructions:
#         instruction = instruction.split()
#         to_move = int(instruction[1])
#         from_stack = int(instruction[3]) - 1
#         to_stack = int(instruction[5]) - 1

#         instruction_list.append([to_move, from_stack, to_stack])

#     return stacks, instruction_list


# def moveThings(stacks: list, instructions: list) -> str:
#     """Takes in a list of lists and instructions and use the instructions to move around data in the list of lists.
#     - 'move 1 from 2 to 1' translates to move one thing from stack 2 to stack 1"""
#     # print(stacks)
#     # print(instructions)

#     print(f"Original: {stacks}")

#     for n in instructions:
#         things_to_move = n[0]

#         moved_stuff = stacks[n[2 - 1]][:things_to_move]
#         moved_stuff.reverse()

#         stacks[n[2 - 1]] = stacks[n[2 - 1]][things_to_move:]
#         # to_stack = stacks[n[3 - 1]]
#         stacks[n[3 - 1]] = stacks[n[3 - 1]] + moved_stuff

#         print(stacks)


# def main():
#     data = getData("test.txt")
#     the_stacks = data[0]
#     the_instructions = data[1]

#     moveThings(stacks=the_stacks, instructions=the_instructions)


# if __name__ == "__main__":
#     main()


def parse_stack_text(stacktext):
    stacks = [""] * 10
    for line in stacktext[:-1]:
        for i, box in enumerate(line[1::4]):
            if box != " ":
                stacks[i + 1] += box
    return stacks


input_data = open("aoc_day5_input.txt").read()
stackt, instructions = [part.split("\n") for part in input_data.split("\n\n")]
stacks = parse_stack_text(stackt)

p1, p2 = stacks[:], stacks[:]
for line in instructions:
    _, n, _, src, _, dest = line.split()
    n = int(n)
    src = int(src)
    dest = int(dest)

    p1[src], p1[dest] = p1[src][n:], p1[src][:n][::-1] + p1[dest]
    p2[src], p2[dest] = p2[src][n:], p2[src][:n] + p2[dest]

print("Part 1:", "".join(s[0] for s in p1 if s))
print("Part 2:", "".join(s[0] for s in p2 if s))
