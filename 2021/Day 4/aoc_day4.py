import re

nums, *tickets = open("aoc_day4_input.txt").read().strip().split("\n\n")
nums = [int(x) for x in nums.split(",")]
tickets = [
    [list(map(int, re.findall("\d+", line))) for line in t.split("\n")] for t in tickets
]

used, winners = set(nums[:4]), set()
for k in nums[4:]:
    used.add(k)
    for (i, tick) in enumerate(tickets):
        if i in winners:
            continue
        if any(all(n in used for n in row) for row in tick) or any(
            all(n in used for n in col) for col in zip(*tick)
        ):
            winners.add(i)
            if len(winners) == 1 or len(winners) == len(tickets):
                print(sum(sum(n for n in line if n not in used) for line in tick) * k)
