import unittest
from collections import Counter
from pathlib import Path

import lib

with open(
    Path(__file__).parent.joinpath("data/test_input.txt"), "r", encoding="utf-8"
) as f:
    test_input_lines = f.read().split("\n")


class Test(unittest.TestCase):
    def test_total_winnings(self):
        self.assertEqual(
            6440,
            lib.total_winnings(
                [
                    ("32T3K", 765),
                    ("KK677", 220),
                    ("KTJJT", 28),
                    ("T55J5", 684),
                    ("QQQJA", 483),
                ]
            ),
        )

    def test_classify_hand_five_of_a_kind(self):
        self.assertEqual(lib.HandType.FiveOfAKind, lib.classify_hand("AAAAA"))

    def test_classify_hand_four_of_a_kind(self):
        self.assertEqual(lib.HandType.FourOfAKind, lib.classify_hand("AA8AA"))

    def test_classify_hand_full_house(self):
        self.assertEqual(lib.HandType.FullHouse, lib.classify_hand("23332"))

    def test_classify_hand_three_of_a_kind(self):
        self.assertEqual(lib.HandType.ThreeOfAKind, lib.classify_hand("TTT98"))

    def test_classify_hand_two_pair(self):
        self.assertEqual(lib.HandType.TwoPair, lib.classify_hand("23432"))

    def test_classify_hand_one_pair(self):
        self.assertEqual(lib.HandType.OnePair, lib.classify_hand("A23A4"))

    def test_classify_hand_high_card(self):
        self.assertEqual(lib.HandType.HighCard, lib.classify_hand("23456"))

    def test_compare_hand(self):
        self.assertEqual(
            lib.is_larger, lib.is_hand_larger("33332", "2AAAA", with_joker=False)
        )

    def test_parse(self):
        hands = lib.parse_lines(test_input_lines)
        self.assertEqual(("32T3K", 765), hands[0])
        self.assertEqual(("QQQJA", 483), hands[-1])

    def test_compare_hands(self):
        self.assertEqual(-1, lib.is_hand_larger("T55J5", "QQQJA", with_joker=False))
        self.assertEqual(1, lib.is_hand_larger("QQQJA", "T55J5", with_joker=False))
        self.assertEqual(-1, lib.is_hand_larger("KK677", "T55J5", with_joker=False))

    def test_is_hand_larger(self):
        sorted_cards = ["32T3K", "KTJJT", "KK677", "T55J5", "QQQJA"]
        # sorted_cards = ["KTJJT", "KK677"]
        for cards1, cards2 in zip(sorted_cards[:-1], sorted_cards[1:]):
            self.assertEqual(
                lib.is_larger,
                lib.is_hand_larger(cards2, cards1, with_joker=False),
                f"{cards2} is larger than {cards1}",
            )
            self.assertEqual(
                lib.is_smaller,
                lib.is_hand_larger(cards1, cards2, with_joker=False),
                f"{cards2} is smaller than {cards1}",
            )

    def test_sort_hands(self):
        hands = lib.parse_lines(test_input_lines)
        hands = lib.sort_hands(hands)
        cards = [hand[0] for hand in hands]
        sorted_cards = ["32T3K", "KTJJT", "KK677", "T55J5", "QQQJA"]
        self.assertEqual(sorted_cards, cards)


class TestJoker(unittest.TestCase):
    def assert_larger(self, larger: str, smaller: str):
        self.assertEqual(
            lib.is_larger, lib.is_hand_larger(larger, smaller, with_joker=True)
        )
        self.assertEqual(
            lib.is_smaller, lib.is_hand_larger(smaller, larger, with_joker=True)
        )

    def test_compare_hands(self):
        self.assert_larger("22222", "J2222")

    def test_classify_hand(self):
        self.assertEqual(
            lib.HandType.FourOfAKind, lib.classify_hand_with_joker("QJJQ2")
        )
        self.assertEqual(
            lib.HandType.FiveOfAKind, lib.classify_hand_with_joker("QJQQJ")
        )
        self.assertEqual(
            lib.HandType.FiveOfAKind, lib.classify_hand_with_joker("JJJJJ")
        )

    def assert_one_of_best_hand(self, cards: str, of_hands: set[str]):
        best_hand = lib.get_best_hand(cards)
        for expected_hand in of_hands:
            try:
                self.assertEqual(Counter(best_hand), Counter(expected_hand))
                return
            except AssertionError:
                pass
        raise AssertionError(
            f"Hand {cards}, with best hand = {best_hand} did not match any of"
            f" the expected hands: {of_hands}"
        )

    def test_get_best_hand_of_many(self):
        self.assert_one_of_best_hand("2345J", {"23452", "23453", "23454", "23455"})
        self.assert_one_of_best_hand("2345J", {"23452", "23453", "23454", "23455"})

    def assert_best_hand(self, expected_cards: str, cards: str):
        self.assertEqual(Counter(expected_cards), Counter(lib.get_best_hand(cards)))

    def test_get_best_hand(self):
        self.assert_best_hand("QQQQ2", "QJJQ2")

    def test_sort_hands(self):
        hands = lib.parse_lines(test_input_lines)
        hands = lib.sort_hands_joker(hands)
        cards = [hand[0] for hand in hands]
        sorted_cards = ["32T3K", "KK677", "T55J5", "QQQJA", "KTJJT"]
        self.assertEqual(sorted_cards, cards)


class TestPart(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(6440, lib.part1(test_input_lines))

    def test_part2(self):
        self.assertEqual(5905, lib.part2(test_input_lines))
