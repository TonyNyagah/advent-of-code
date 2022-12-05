# read the input data
lines = [
    "[D]",
    "[N] [C]",
    "[Z] [M] [P]",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]

# parse the input data
stacks = []
for line in lines[:3]:
    stack = []
    for crate in line.split():
        crate = crate.replace("[", "").replace("]", "")
        if crate:
            stack.append(crate)
    stacks.append(stack)

instructions = lines[3:]

# simulate the rearrangement procedure
for instruction in instructions:
    # parse the instruction
    words = instruction.split()
    amount = int(words[1])
    from_stack = int(words[3])
    to_stack = int(words[5])

    # move the crates
    for i in range(amount):
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)

# print the top crates in each stack
for i, stack in enumerate(stacks):
    print("Stack", i + 1, ":", stack[-1])
