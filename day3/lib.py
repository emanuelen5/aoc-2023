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

    def __hash__(self) -> int:
        return hash((self.parsed, self.start_pos, self.next_pos))


def get_number_at_position(lines: list[str], pos: Pos) -> Parsed:
    line = lines[pos.row]
    width = len(line)
    if not line[pos.col].isdigit():
        return Parsed(
            "", pos, next_pos=Pos(pos.row, pos.col + 1).maybe_adjust_eol(width)
        )

    start = pos.col
    while start > 0 and line[start - 1].isdigit():
        start -= 1

    end = pos.col
    while end < len(line) and line[end].isdigit():
        end += 1

    return Parsed(
        line[start : end], Pos(pos.row, start), next_pos=Pos(pos.row, end).maybe_adjust_eol(width)
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


def find_gear_on_line(line: str) -> tuple[int, ...]:
    found_gears = []

    last_index = 0
    try:
        while found := line.index("*", last_index + 1):
            found_gears.append(found)
            last_index = found
    except ValueError:
        pass

    return tuple(found_gears)


def find_all_gears(lines: list[str]) -> tuple[Pos, ...]:
    return tuple(
        Pos(row, col)
        for row, line in enumerate(lines)
        for col in find_gear_on_line(line)
    )


def adjacent_numbers(padded_lines: list[str], gear: Pos) -> list[int]:
    row = gear.row
    outer_left_col = gear.col - 1
    outer_right_col = gear.col + 1

    numbers = []
    for (row, col) in (
        (row - 1, outer_left_col),
        (row, outer_left_col),
        (row + 1, outer_left_col),
        (row - 1, outer_right_col),
        (row - 1, gear.col),
        (row + 1, gear.col),
        (row, outer_right_col),
        (row + 1, outer_right_col),
    ):
        num = get_number_at_position(padded_lines, Pos(row, col))
        if num:
            numbers.append(num)
    return list(sorted(int(n) for n in set(numbers)))


def find_all_gear_numbers(padded_lines: list[str]) -> list[list[int]]:
    numbers = []
    gears = find_all_gears(padded_lines)
    for gear in gears:
        a_nums = adjacent_numbers(padded_lines, gear)
        if a_nums:
            numbers.append(a_nums)

    return numbers


def part2(lines: list[str]) -> int:
    padded_lines = pad_input(lines)

    sum = 0
    number_groups = find_all_gear_numbers(padded_lines)
    for number_group in number_groups:
        if len(number_group) == 2:
            sum += number_group[0] *  number_group[1]
        elif len(number_group) > 2:
            raise ValueError("Too many numbers touching gear!")

    return sum
