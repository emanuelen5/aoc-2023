def first_and_last_number(s: str) -> str:
    from_start = (c for c in s if c.isdigit())
    from_back = (c for c in reversed(s) if c.isdigit())
    return next(from_start) + next(from_back)


def as_int(s: str) -> int:
    return int(s)


def first_and_last_number_as_int(s: str) -> int:
    return as_int(first_and_last_number(s))


number_mapping_orig = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

reversed_number_mapping = {
    name[::-1]: num for name, num in number_mapping_orig.items()
}


def find_first_number(s: str, number_mapping: dict[str, int]) -> int:
    min_index = len(s)
    number = None
    for needle, num in number_mapping.items():
        try:
            index = s.index(needle)
            if index < min_index:
                min_index = index
                number = num
        except ValueError:
            continue
    assert number is not None
    return number


def first_number2(s: str) -> int:
    return find_first_number(s, number_mapping_orig)


def last_number2(s: str) -> int:
    s = s[::-1]
    return find_first_number(s, reversed_number_mapping)


def first_and_last_number2_as_int(s: str) -> int:
    return first_number2(s) * 10 + last_number2(s)
