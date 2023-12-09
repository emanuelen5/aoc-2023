import re


def split_line(s: str) -> tuple[str, str, str]:
    return tuple(part.strip() for part in re.split("[:|]", s))


def line_winning_numbers(line: str):
    card, winning, yours = split_line(line)
    winning_numbers = {int(n) for n in winning.split(" ") if n}
    my_numbers = {int(n) for n in yours.split(" ") if n}

    return winning_numbers.intersection(my_numbers)


def part1(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        winners = line_winning_numbers(line)
        count = len(winners)
        if count > 0:
            score = 2 ** (count - 1)
            sum += score

    return sum
