from dataclasses import dataclass


def is_symbol(s: str) -> bool:
    return s not in ".1234567890"


def pad_input(lines: list[str]) -> list[str]:
    padded_lines = list("." + line + "." for line in lines)

    width = len(padded_lines[0])

    pad_row = "." * width

    padded_lines.insert(0, pad_row)
    padded_lines.append(pad_row)

    return padded_lines


@dataclass(frozen=True)
class Pos:
    row: int
    col: int

    def maybe_adjust_eol(self, width: int):
        if self.col < width:
            return self

        return self.__class__(self.row + 1, 0)


@dataclass
class Parsed:
    parsed: str
    start_pos: Pos
    next_pos: Pos

    def __len__(self) -> int:
        return len(self.parsed)

    def __int__(self) -> int:
        return int(self.parsed)

    def __bool__(self) -> bool:
        return bool(self.parsed)


def get_number_at_position(lines: list[str], pos: Pos) -> Parsed:
    line = lines[pos.row]
    width = len(line)
    if not line[pos.col].isdigit():
        return Parsed(
            "", pos, next_pos=Pos(pos.row, pos.col + 1).maybe_adjust_eol(width)
        )

    end = pos.col
    while end < len(line) and line[end].isdigit():
        end += 1

    return Parsed(
        line[pos.col : end], pos, next_pos=Pos(pos.row, end).maybe_adjust_eol(width)
    )


def neighbors_symbol(padded_lines: list[str], parsed: Parsed) -> bool:
    def is_symbol_at_pos(row: int, col: int) -> bool:
        return is_symbol(padded_lines[row + 1][col + 1])

    row = parsed.start_pos.row
    start_col = parsed.start_pos.col
    outer_left_col = parsed.start_pos.col - 1
    outer_right_col = parsed.start_pos.col + len(parsed)

    # symbol above
    for c in padded_lines[row][start_col + 1 : outer_right_col + 1]:
        if is_symbol(c):
            return True

    # symbol below
    for c in padded_lines[row + 2][start_col + 1 : outer_right_col + 1]:
        if is_symbol(c):
            return True

    return any(
        [
            is_symbol_at_pos(row - 1, outer_left_col),
            is_symbol_at_pos(row, outer_left_col),
            is_symbol_at_pos(row + 1, outer_left_col),
            is_symbol_at_pos(row - 1, outer_right_col),
            is_symbol_at_pos(row, outer_right_col),
            is_symbol_at_pos(row + 1, outer_right_col),
        ]
    )

def part1(lines: list[str]) -> int:
    padded_lines = pad_input(lines)

    sum = 0
    pos = Pos(0, 0)
    while pos.row < len(lines):
        parsed = get_number_at_position(lines, pos)
        if parsed and neighbors_symbol(padded_lines, parsed):
            sum += int(parsed)

        pos = parsed.next_pos

    return sum
