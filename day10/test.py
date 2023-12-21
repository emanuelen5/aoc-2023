import unittest
from pathlib import Path

import lib

with open(
    Path(__file__).parent.joinpath("data/test_input.txt"), "r", encoding="utf-8"
) as f:
    test_input_lines = f.read().split("\n")

map = test_input_lines
start_pos = (2, 0)


class Test(unittest.TestCase):
    def test_pad(self):
        self.assertEqual(".......", lib.pad(map)[0])
        self.assertEqual("...F7..", lib.pad(map)[1])

    def test_find_start(self):
        self.assertEqual(start_pos, lib.find_start(map))

    def test_turn_invalid(self):
        with self.assertRaises(lib.MoveException):
            lib.turn(".", lib.Dir.right)

    def test_forward(self):
        self.assertEqual(
            ((0, 1), lib.Dir.right),
            lib.forward("-", ((0, 0), lib.Dir.right)),
        )

    def test_start_seed(self):
        self.assertCountEqual(
            [
                ((2, 1), lib.Dir.right),
                ((3, 0), lib.Dir.down),
            ],
            lib.start_seed(map),
        )

    def test_part1(self):
        self.assertEqual(8, lib.part1(map))
