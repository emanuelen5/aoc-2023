def first_and_last_number(s: str) -> str:
    from_start = (c for c in s if c.isdigit())
    from_back = (c for c in reversed(s) if c.isdigit())
    return next(from_start) + next(from_back)


def as_int(s: str) -> int:
    return int(s)


def first_and_last_number_as_int(s: str) -> int:
    return as_int(first_and_last_number(s))
