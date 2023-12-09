import unittest
from pathlib import Path

import lib
from lib import Parsed, Pos

with open(
    Path(__file__).parent.joinpath("data/test_input.txt"), "r", encoding="utf-8"
) as f:
    test_input_lines = f.read().split("\n")

padded_lines = lib.pad_input(test_input_lines)


class TestArray(unittest.TestCase):
    def test_is_symbol_not_symbols(self):
        for c in "1234567890.":
            self.assertFalse(lib.is_symbol(c), msg=f"{c} should not be a symbol")

    def test_is_symbol_symbols(self):
        for c in "!@#$%^&*()":
            self.assertTrue(lib.is_symbol(c), msg=f"{c} should be a symbol")

    def test_pad_lines(self):
        # fmt: off
        self.assertEqual([
            "...",
            "...",
            "..."
        ], lib.pad_input(["."]))
        self.assertEqual([
            "...",
            ".#.",
            "..."
        ], lib.pad_input(["#"]))
        # fmt: on


class TestParse(unittest.TestCase):
    def check_parsed(self, num: int, parsed: Parsed):
        if num is None:
            self.assertEqual("", parsed.parsed)
        else:
            self.assertEqual(num, int(parsed))

    def test_parse_number_int(self):
        self.check_parsed(467, lib.get_number_at_position(test_input_lines, Pos(0, 0)))
        self.check_parsed(114, lib.get_number_at_position(test_input_lines, Pos(0, 5)))

    def test_parse_number(self):
        self.assertEqual(
            Parsed("58", start_pos=Pos(5, 7), next_pos=Pos(5, 9)),
            lib.get_number_at_position(test_input_lines, Pos(5, 7)),
        )

        self.assertEqual(
            Parsed("58", start_pos=Pos(5, 7), next_pos=Pos(5, 9)),
            lib.get_number_at_position(test_input_lines, Pos(5, 8)),
        )

    def test_parse_null(self):
        self.check_parsed(None, lib.get_number_at_position(test_input_lines, Pos(1, 0)))

    def test_parse_number_eol(self):
        self.assertEqual(
            Parsed("", start_pos=Pos(0, 9), next_pos=Pos(1, 0)),
            lib.get_number_at_position(test_input_lines, Pos(0, 9)),
        )


class TestFindSymbol(unittest.TestCase):
    def test_neighbors_symbol(self):
        self.assertTrue(
            lib.neighbors_symbol(padded_lines, Parsed("467", Pos(0, 0), Pos(0, 3)))
        )

    def test_neighbors_symbol_above(self):
        self.assertTrue(
            lib.neighbors_symbol(padded_lines, Parsed("35", Pos(2, 2), Pos(2, 4)))
        )

    def test_does_not_neighbor_symbol(self):
        self.assertFalse(
            lib.neighbors_symbol(padded_lines, Parsed("114", Pos(0, 5), Pos(0, 8)))
        )


class TestFindGears(unittest.TestCase):
    def test_find_on_line(self):
        self.assertEqual((3,), lib.find_gear_on_line(test_input_lines[1]))

    def test_find_all_gears(self):
        self.assertEqual(
            (Pos(1, 3), Pos(4, 3), Pos(8, 5)), lib.find_all_gears(test_input_lines)
        )


class TestFindNumbers(unittest.TestCase):
    def test_first_gear(self):
        self.assertListEqual(
            [35, 467],
            lib.adjacent_numbers(test_input_lines, Pos(1, 3)),
        )

    def test_find_all_numbers(self):
        self.assertEqual(
            [
                [35, 467],
                [617],
                [598, 755],
            ],
            lib.find_all_gear_numbers(padded_lines)
        )

class TestPart(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(4361, lib.part1(test_input_lines))

    def test_part2(self):
        self.assertEqual(467835, lib.part2(test_input_lines))


tc = unittest.TestCase()
