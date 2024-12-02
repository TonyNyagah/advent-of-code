def read_input(filename: str) -> list[list[int]]:
    """
    Reads a file and returns a list of lists of ints.

    The file is expected to contain lines of space-separated integers.
    Each line is converted to a list of ints and returned as a list.
    """
    data = [*map(lambda x: list(map(int, x.split())), open(filename))]
    return data


def is_safe(row: list[int]) -> bool:
    """
    Check if a row of numbers is safe according to the problem rules.

    A row is safe if all consecutive differences are either increasing by 1, 2, or 3,
    or decreasing by 1, 2, or 3.

    Args:
        row (list): A list of numbers.

    Returns:
        bool: True if the row is safe, False otherwise.
    """

    # Calculate consecutive differences
    differences = [row[i + 1] - row[i] for i in range(len(row) - 1)]

    # Check if all differences are increasing or decreasing by 1, 2, or 3
    increasing_differences = {1, 2, 3}
    decreasing_differences = {-1, -2, -3}

    return (
        set(differences) <= increasing_differences
        or set(differences) <= decreasing_differences
    )


def count_safe_reports(reports: list[list[int]], dampener: bool = False) -> int:
    """
    Count the number of safe reports in the given data.

    If dampener is False (default), count the number of rows that are safe
    according to the problem rules. If dampener is True, count the number of rows
    that can be made safe by removing a single element.

    Args:
        reports (list): A list of lists of numbers.
        dampener (bool): If True, count rows that can be made safe by removing a
            single element. Defaults to False.

    Returns:
        int: The number of safe reports.
    """
    if dampener:
        return sum(
            [
                any([is_safe(row[:i] + row[i + 1 :]) for i in range(len(row))])
                for row in reports
            ]
        )

    return sum([is_safe(row) for row in reports])


test_input = read_input("test.txt")
input = read_input("input.txt")
# Test
print(count_safe_reports(test_input))
# Part 1
print(count_safe_reports(input))
# Part 2
print(count_safe_reports(input, dampener=True))
