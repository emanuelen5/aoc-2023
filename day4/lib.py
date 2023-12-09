import copy
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


class Slots:
    def __init__(self, lines: list[str]) -> None:
        self.state = [1] * len(lines)
        self.cards = len(lines)
        self.extra_cards = 0

    def process_card(self, lines: list[str], card: int) -> "Slots":
        inst = copy.deepcopy(self)

        new_cards = len(line_winning_numbers(lines[card]))
        inst.cards += new_cards
        inst.extra_cards += new_cards

        copies = inst.state[card]
        next_index = card + 1
        for i in range(next_index, next_index + new_cards):
            inst.state[i] += copies

        return inst


def part2(lines: list[str]) -> int:
    slots = Slots(lines)
    for i in range(len(lines)):
        slots = slots.process_card(lines, card=i)

    return sum(slots.state)
