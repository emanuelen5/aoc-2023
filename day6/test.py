import unittest
from pathlib import Path

import lib

with open(
    Path(__file__).parent.joinpath("data/test_input.txt"), "r", encoding="utf-8"
) as f:
    test_input_lines = f.read().split("\n")


class Test(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(((7, 15, 30), (9, 40, 200)), lib.parse_input(test_input_lines))

    def test_bisect(self):
        def f(i):
            return i > 0

        self.assertEqual(1, lib.bisect(f, -100, 100))
        self.assertEqual(1, lib.bisect(f, -1, 1))

    def test_distance_by_powerup(self):
        self.assertEqual(0, lib.distance_by_powerup(total_race_time=7, powerup_time=0))
        self.assertEqual(6, lib.distance_by_powerup(total_race_time=7, powerup_time=1))
        self.assertEqual(10, lib.distance_by_powerup(total_race_time=7, powerup_time=2))

    def test_smallest_winning_powerup(self):
        self.assertEqual(2, lib.smallest_winning_powerup(t=7, record=9))
        self.assertEqual(4, lib.smallest_winning_powerup(t=15, record=40))
        self.assertEqual(11, lib.smallest_winning_powerup(t=30, record=200))

    def test_get_winning_times_count(self):
        self.assertEqual(4, lib.get_winning_times_count(t=7, record=9))
        self.assertEqual(8, lib.get_winning_times_count(t=15, record=40))
        self.assertEqual(9, lib.get_winning_times_count(t=30, record=200))

    def test_part1(self):
        self.assertEqual(288, lib.part1(test_input_lines))


tc = unittest.TestCase()
