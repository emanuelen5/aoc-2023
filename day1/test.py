import unittest
from pathlib import Path

import lib

_dir = Path(__file__).parent

with open(_dir.joinpath("data/test_input.txt"), "r", encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")

with open(_dir.joinpath("data/test_input2.txt"), "r", encoding="utf-8") as f:
    test_input2_lines = f.read().split("\n")


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


class TestFirstNumber(unittest.TestCase):
    def test_number(self):
        self.assertEqual(1, lib.first_number2("1two"))

    def test_letter(self):
        self.assertEqual(2, lib.first_number2("two1"))
        self.assertEqual(1, lib.first_number2("1two3"))


class TestLastNumber(unittest.TestCase):
    def test_number(self):
        self.assertEqual(5, lib.last_number2("onetwothree5fif"))

    def test_letter(self):
        self.assertEqual(3, lib.last_number2("onetwo5three"))
        self.assertEqual(3, lib.last_number2("1nsetwo5three3"))
        self.assertEqual(6, lib.last_number2("cgpzm2sevenone68636"))


class TestFile2(unittest.TestCase):
    def test_lines(self):
        self.assertEqual(29, lib.first_and_last_number2_as_int(test_input2_lines[0]))
        self.assertEqual(83, lib.first_and_last_number2_as_int(test_input2_lines[1]))
        self.assertEqual(13, lib.first_and_last_number2_as_int(test_input2_lines[2]))
        self.assertEqual(24, lib.first_and_last_number2_as_int(test_input2_lines[3]))
        self.assertEqual(42, lib.first_and_last_number2_as_int(test_input2_lines[4]))
        self.assertEqual(14, lib.first_and_last_number2_as_int(test_input2_lines[5]))
        self.assertEqual(76, lib.first_and_last_number2_as_int(test_input2_lines[6]))

    def test_example(self):
        self.assertEqual(26, lib.first_and_last_number2_as_int("cgpzm2sevenone68636"))


tc = unittest.TestCase()
