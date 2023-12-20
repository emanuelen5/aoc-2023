import unittest
from pathlib import Path

import lib

with open(
    Path(__file__).parent.joinpath("data/test_input.txt"), "r", encoding="utf-8"
) as f:
    test_input_lines = f.read().split("\n")


class Test(unittest.TestCase):
    def test_diff(self):
        histories = lib.parse(test_input_lines)
        self.assertListEqual([3, 3, 3, 3, 3], lib.diff(histories[0]))

    def test_predict(self):
        histories = lib.parse(test_input_lines)
        self.assertEqual(18, lib.predict(histories[0]))
        self.assertEqual(28, lib.predict(histories[1]))
        self.assertEqual(68, lib.predict(histories[2]))

    def test_part1(self):
        self.assertEqual(114, lib.part1(test_input_lines))
