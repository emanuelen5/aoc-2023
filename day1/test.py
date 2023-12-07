import unittest
from pathlib import Path

import lib

with open(Path(__file__).parent.joinpath("data/test_input.txt"), 'r', encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")


class TestFirstAndLastNumber(unittest.TestCase):
    def test_simple(self):
        self.assertEqual("14", lib.first_and_last_number("14"))

    def test_in_between(self):
        self.assertEqual("14", lib.first_and_last_number("1asdasd4"))

    def test_around(self):
        self.assertEqual("14", lib.first_and_last_number("asd1asdasd4asd"))


class TestAsInt(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(14, lib.as_int("14"))


class TestFile(unittest.TestCase):
    def test_lines(self):
        self.assertEqual(12, lib.first_and_last_number_as_int(test_input_lines[0]))
        self.assertEqual(38, lib.first_and_last_number_as_int(test_input_lines[1]))
        self.assertEqual(15, lib.first_and_last_number_as_int(test_input_lines[2]))
        self.assertEqual(77, lib.first_and_last_number_as_int(test_input_lines[3]))

tc = unittest.TestCase()
