import unittest
from pathlib import Path

import lib

with open(
    Path(__file__).parent.joinpath("data/test_input.txt"), "r", encoding="utf-8"
) as f:
    test_input_lines = f.read().split("\n")


class Test(unittest.TestCase):
    def test_line_score(self):
        self.assertEqual(
            {41, 48, 83, 86, 17}, lib.line_winning_numbers(test_input_lines[0])
        )
        self.assertEqual({32, 61}, lib.line_winning_numbers(test_input_lines[1]))
        self.assertEqual({1, 21}, lib.line_winning_numbers(test_input_lines[2]))
        self.assertEqual({84}, lib.line_winning_numbers(test_input_lines[3]))
        self.assertEqual({}, lib.line_winning_numbers(test_input_lines[4]))
        self.assertEqual({}, lib.line_winning_numbers(test_input_lines[5]))


tc = unittest.TestCase()
