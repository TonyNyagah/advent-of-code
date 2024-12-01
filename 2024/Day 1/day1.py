def read_input(filename: str) -> tuple[list[int], list[int]]:
    data = [*map(int, open(filename).read().split())]
    return sorted(data[0::2]), sorted(data[1::2])


def calculate_total_distance(left_list: list[int], right_list: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(left_list, right_list))


def calculate_similarity_score(left_list: list[int], right_list: list[int]) -> int:
    return sum(a * right_list.count(a) for a in left_list)


left_list, right_list = read_input("aoc_day1_input.txt")
# Part 1
print(calculate_total_distance(left_list, right_list))
# Part 2
print(calculate_similarity_score(left_list, right_list))
