rot90 = lambda A: [*map(list, zip(*A[::-1]))]

grid = [[*map(int, x.strip())] for x in open("aoc_day8_input.txt")]
part1 = [[0 for _ in x] for x in grid]
part2 = [[1 for _ in x] for x in grid]

for _ in range(4):
    for x, y in [(x, y) for x in range(99) for y in range(99)]:
        lower = [t < grid[x][y] for t in grid[x][y + 1 :]]

        part1[x][y] |= all(lower)
        part2[x][y] *= len(lower) if all(lower) else lower.index(0) + 1

    grid, part1, part2 = map(rot90, [grid, part1, part2])

print(sum(map(sum, part1)), max(map(max, part2)))
