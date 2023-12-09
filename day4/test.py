import unittest
from pathlib import Path

import lib

with open(
    Path(__file__).parent.joinpath("data/test_input.txt"), "r", encoding="utf-8"
) as f:
    test_input_lines = f.read().split("\n")


class Test(unittest.TestCase):
    def test_split_line(self):
        self.assertEqual(
            ("Card 1", "41 48 83 86 17", "83 86  6 31 17  9 48 53"),
            lib.split_line(test_input_lines[0]),
        )

    def test_line_score(self):
        self.assertEqual(
            {48, 83, 17, 86}, lib.line_winning_numbers(test_input_lines[0])
        )
        self.assertEqual({32, 61}, lib.line_winning_numbers(test_input_lines[1]))
        self.assertEqual({1, 21}, lib.line_winning_numbers(test_input_lines[2]))
        self.assertEqual({84}, lib.line_winning_numbers(test_input_lines[3]))
        self.assertEqual(set(), lib.line_winning_numbers(test_input_lines[4]))
        self.assertEqual(set(), lib.line_winning_numbers(test_input_lines[5]))


class TestPart(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(13, lib.part1(test_input_lines))

    def test_part2(self):
        self.assertEqual(30, lib.part2(test_input_lines))


class TestBins(unittest.TestCase):
    def test_process_cards(self):
        slots = lib.Slots(test_input_lines)
        self.assertEqual(0, slots.extra_cards)
        self.assertEqual(6, slots.cards)
        self.assertEqual([1] * 6, slots.state)

        new_slots = slots.process_card(test_input_lines, card=0)
        self.assertEqual(4, new_slots.extra_cards)
        self.assertEqual(10, new_slots.cards)
        self.assertEqual([1, 2, 2, 2, 2, 1], new_slots.state)


tc = unittest.TestCase()
