import unittest
from pathlib import Path

import lib
from lib import is_game_feasible, parse_game_id, parse_line

with open(
    Path(__file__).parent.joinpath("data/test_input.txt"), "r", encoding="utf-8"
) as f:
    test_input_lines = f.read().split("\n")


class Test(unittest.TestCase):
    def test_is_game_feasible(self):
        self.assertEqual(True, is_game_feasible({"red": 4, "green": 2, "blue": 6}))
        self.assertEqual(False, is_game_feasible({"red": 44, "blue": 6}))
        self.assertEqual(False, is_game_feasible({"red": 4, "green": 2, "blue": 100}))

    def test_parse_line(self):
        self.assertEqual(
            {"red": 4, "green": 2, "blue": 6}, parse_line(test_input_lines[0])
        )

    def test_parse_game_id(self):
        self.assertEqual(
            1, parse_game_id("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        )

    def test_parse_game_id_is_large(self):
        self.assertEqual(
            200001,
            parse_game_id(
                "Game 200001: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
            ),
        )

    def test_get_power(self):
        self.assertEqual(
            48,
            lib.get_power({"red": 4, "green": 2, "blue": 6})
        )


class TestPart(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(8, lib.part1(test_input_lines))

    def test_part2(self):
        self.assertEqual(2286, lib.part2(test_input_lines))
