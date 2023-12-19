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


regular_rank = {
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

joker_rank = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
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


def is_hand_larger(cards1: str, cards2: str, with_joker: bool) -> int:
    if with_joker:
        card_rank = joker_rank
        hand1_class = classify_hand_with_joker(cards1)
        hand2_class = classify_hand_with_joker(cards2)
    else:
        card_rank = regular_rank
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


def classify_hand_with_joker(cards: str) -> HandType:
    best_hand = get_best_hand(cards)
    return classify_hand(best_hand)


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


def build_best_hand(cards: str, joker_count: int) -> str:
    if joker_count == 0:
        return cards

    best_hand = cards
    best_hand_class = classify_hand(cards)
    for replace_card in set(cards):
        new_hand = build_best_hand(cards + replace_card, joker_count - 1)
        new_hand_class = classify_hand(new_hand)
        if new_hand_class > best_hand_class:
            best_hand = new_hand
            best_hand_class = new_hand_class

    return best_hand


def get_best_hand(cards: str) -> str:
    if "J" not in cards:
        return cards

    cards_and_counts = Counter(cards)
    joker_count = cards_and_counts["J"]

    cards_without_jokers = cards.replace("J", "")

    if len(cards_without_jokers) == 0:
        return "AAAAA"

    return build_best_hand(cards_without_jokers, joker_count)


def total_winnings(sorted_hands: tuple[hand_t, int]):
    return sum(bid * (index + 1) for index, (hand, bid) in enumerate(sorted_hands))


def sort_hands(hands):
    card_key_compare = functools.cmp_to_key(
        lambda a, b: is_hand_larger(a, b, with_joker=False)
    )

    def hand_key_compare(hand: tuple[str, int]):
        cards, _ = hand
        return card_key_compare(cards)

    return sorted(hands, key=hand_key_compare)


def sort_hands_joker(hands):
    card_key_compare = functools.cmp_to_key(
        lambda a, b: is_hand_larger(a, b, with_joker=True)
    )

    def hand_key_compare(hand: tuple[str, int]):
        cards, _ = hand
        return card_key_compare(cards)

    return sorted(hands, key=hand_key_compare)


def part1(lines: list[str]) -> int:
    hands = parse_lines(lines)
    sorted_hands = sort_hands(hands)
    return total_winnings(sorted_hands)


def part2(lines: list[str]) -> int:
    hands = parse_lines(lines)
    sorted_hands = sort_hands_joker(hands)
    return total_winnings(sorted_hands)
