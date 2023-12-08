def is_symbol(s: str) -> bool:
    return s not in ".1234567890"


def pad_input(lines: list[str]) -> list[str]:
    padded_lines = list("." + line + "." for line in lines)

    width = len(padded_lines[0])

    pad_row = "." * width

    padded_lines.insert(0, pad_row)
    padded_lines.append(pad_row)

    return padded_lines
