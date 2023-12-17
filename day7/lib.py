import enum
import functools
from collections import Counter

hand_t = str


def parse_lines(lines: list[str]) -> tuple[hand_t, int]:
    hands = []
    for line in lines:
        hand, bet = line.split()
        hands.append((hand, int(bet)))
    return hands


card_rank = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class HandType(enum.IntEnum):
    HighCard = 1
    OnePair = 2
    TwoPair = 3
    ThreeOfAKind = 4
    FullHouse = 5
    FourOfAKind = 6
    FiveOfAKind = 7


is_larger = 1
is_smaller = -1


def is_hand_larger(cards1: str, cards2: str) -> int:
    hand1_class = classify_hand(cards1)
    hand2_class = classify_hand(cards2)

    if hand1_class != hand2_class:
        return hand1_class - hand2_class

    for card1, card2 in zip(cards1, cards2):
        if card_rank[card1] > card_rank[card2]:
            return is_larger
        if card_rank[card1] < card_rank[card2]:
            return is_smaller

    raise ValueError(
        "Could not determine which hand was best." f" Got {cards1=} vs {cards2=}"
    )


def classify_hand(cards: str) -> HandType:
    cards_and_counts = Counter(cards)
    card_counts = tuple(count for count in cards_and_counts.values())

    if 5 in card_counts:
        return HandType.FiveOfAKind
    if 4 in card_counts:
        return HandType.FourOfAKind
    if 3 in card_counts and 2 in card_counts:
        return HandType.FullHouse
    if 3 in card_counts:
        return HandType.ThreeOfAKind

    pair_count = sum(1 for card_count in card_counts if card_count == 2)
    if pair_count == 2:
        return HandType.TwoPair
    if pair_count == 1:
        return HandType.OnePair

    return HandType.HighCard


def total_winnings(sorted_hands: tuple[hand_t, int]):
    return sum(bid * (index + 1) for index, (hand, bid) in enumerate(sorted_hands))


def sort_hands(hands):
    return sorted(hands, key=lambda h: functools.cmp_to_key(is_hand_larger)(h[0]))


def part1(lines: list[str]) -> int:
    hands = parse_lines(lines)
    sorted_hands = sort_hands(hands)
    return total_winnings(sorted_hands)
