import unittest
from pathlib import Path

import lib

with open(
    Path(__file__).parent.joinpath("data/test_input.txt"), "r", encoding="utf-8"
) as f:
    test_input_lines = f.read().split("\n")


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


tc = unittest.TestCase()
