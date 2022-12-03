# The way I'm putting stuff into functions is dumb and I know it


def getData(txt_file) -> list:
    """Get data from a text file."""
    with open(txt_file, "r") as f:
        data_list = f.read().splitlines()
    return data_list


def partOneScores() -> dict:
    """The hard-coded results for part 1 🤷‍♂️"""
    SCORES = {
        "A X": 3 + 1,
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 6,
        "C Y": 2 + 0,
        "C Z": 3 + 3,
    }
    return SCORES


def partTwoScores() -> dict:
    """The hard-coded results for part 2 🤷‍♂️"""
    SCORES = {
        "A X": 0 + 3,
        "A Y": 3 + 1,
        "A Z": 6 + 2,
        "B X": 0 + 1,
        "B Y": 3 + 2,
        "B Z": 6 + 3,
        "C X": 0 + 2,
        "C Y": 3 + 3,
        "C Z": 6 + 1,
    }
    return SCORES


def scoreGeneration(data: list, score_dict: dict) -> int:
    """Takes in a list of match results, compares each result to the score for the given hand and returns a total score."""
    all_scores = []

    for i in data:
        if i in score_dict:
            all_scores.append(score_dict[i])
        else:
            all_scores.append(0)

    return all_scores


def totalScore(data: list) -> int:
    return sum(data)


if __name__ == "__main__":
    data = getData("aoc_day2_input.txt")
    part_one_score_sheet = partOneScores()
    part_two_score_sheet = partTwoScores()

    all_part_one_scores = scoreGeneration(data, part_one_score_sheet)
    all_part_two_scores = scoreGeneration(data, part_two_score_sheet)

    part_one_total_score = totalScore(all_part_one_scores)
    part_two_total_score = totalScore(all_part_two_scores)

    print(f"Part one total score: {part_one_total_score}")
    print(f"Part two total score: {part_two_total_score}")
