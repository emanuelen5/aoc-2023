import unittest
from pathlib import Path

import lib

_dir = Path(__file__).parent

with open(_dir.joinpath("data/test_input.txt"), "r", encoding="utf-8") as f:
    test_input_lines = f.read().split("\n")
with open(_dir.joinpath("data/test_input_part2.txt"), "r", encoding="utf-8") as f:
    test_input2_lines = f.read().split("\n")


class Test(unittest.TestCase):
    def test_parse(self):
        lr, network = lib.parse(test_input_lines)
        self.assertEqual("RL", lr)
        self.assertEqual(7, len(network))
        self.assertIn("AAA", network)
        self.assertIn("ZZZ", network)

    def test_nodes_filled(self):
        _, network = lib.parse(test_input_lines)
        self.assertIsNotNone(network["AAA"].left)
        self.assertIsNotNone(network["AAA"].right)

        self.assertIsNotNone(network["AAA"].left.left)
        self.assertIsNotNone(network["AAA"].left.right)
        self.assertIsNotNone(network["AAA"].right.left)
        self.assertIsNotNone(network["AAA"].right.right)

    def test_parse_network_line(self):
        self.assertEqual(
            ("AAA", "BBB", "CCC"), lib.parse_network_line("AAA = (BBB, CCC)")
        )

    def test_lr_generator(self):
        lr = lib.lr_generator("LR")
        self.assertEqual("L", next(lr))
        self.assertEqual("R", next(lr))
        self.assertEqual("L", next(lr))

    def test_part1(self):
        self.assertEqual(2, lib.part1(test_input_lines))

    def test_part2(self):
        self.assertEqual(6, lib.part2(test_input2_lines))
