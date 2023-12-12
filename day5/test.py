import unittest
from pathlib import Path

import lib

with open(
    Path(__file__).parent.joinpath("data/test_input.txt"), "r", encoding="utf-8"
) as f:
    test_input_lines = f.read().split("\n")


class TestParse(unittest.TestCase):
    def test_line_to_ints(self):
        self.assertEqual((-1, 2, 3, 40), lib.line_to_ints("  -1   2   3  40  "))

    def test_parse(self):
        parse = lib.parse_input(test_input_lines)
        self.assertEqual((79, 14, 55, 13), parse.seeds)
        self.assertEqual(7, len(parse.stages))
        self.assertEqual(2, len(parse.stages[0].maps))
        self.assertEqual(3, len(parse.stages[1].maps))
        self.assertEqual(4, len(parse.stages[2].maps))
        self.assertEqual(2, len(parse.stages[3].maps))
        self.assertEqual(3, len(parse.stages[4].maps))
        self.assertEqual(2, len(parse.stages[5].maps))
        self.assertEqual(2, len(parse.stages[6].maps))

    def test_parse_maps(self):
        parse = lib.parse_input(test_input_lines)
        self.assertEqual(
            lib.Converter([lib.Map(50, 98, 2), lib.Map(52, 50, 48)]), parse.stages[0]
        )
        self.assertEqual(
            lib.Converter([lib.Map(60, 56, 37), lib.Map(56, 93, 4)]), parse.stages[6]
        )


class TestMap(unittest.TestCase):
    def test_convert(self):
        map = lib.Map(101, 1, 5)
        self.assertEqual(0, map.map(0))
        self.assertEqual(101, map.map(1))
        self.assertEqual(104, map.map(4))
        self.assertEqual(105, map.map(5))


class TestConverter(unittest.TestCase):
    def test_map(self):
        converter = lib.Converter([lib.Map(50, 98, 2), lib.Map(52, 50, 48)])
        self.assertEqual(14, converter.map(14))
        self.assertEqual(13, converter.map(13))
        self.assertEqual(81, converter.map(79))
        self.assertEqual(57, converter.map(55))


class TestPart(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(35, lib.part1(test_input_lines))


tc = unittest.TestCase()
