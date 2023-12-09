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


tc = unittest.TestCase()
