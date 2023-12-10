import collections

colors = {"red": 12, "green": 13, "blue": 14}


def parse_line(line):
    [game, cubes] = line.split(": ")
    draws = cubes.split("; ")
    max_colors = collections.defaultdict(lambda: 0)
    for draw in draws:
        cubes = draw.split(", ")
        for cube in cubes:
            [no, col] = cube.split(" ")
            no = int(no)
            max_colors[col] = max(max_colors[col], no)
    return max_colors


def parse_game_id(line):
    semicolon_index = line.index(":")
    game_index = line[5:semicolon_index]
    game_index = int(game_index)
    return game_index


def is_game_feasible(max_colors):
    feasible = True
    for [color, number] in max_colors.items():
        if max_colors[color] > colors[color]:
            feasible = False
    return feasible


def fewest_cubes(line):
    [game, cubes] = line.split(": ")
    draws = cubes.split("; ")
    fewest_cubes = collections.defaultdict(lambda: 0)
    for draw in draws:
        cubes = draw.split(", ")
        for cube in cubes:
            [no, col] = cube.split(" ")
            no = int(no)
            fewest_cubes[col] = max(fewest_cubes[col], no)
    return fewest_cubes


def part1(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        max_colors = parse_line(line)
        game_id = parse_game_id(line)
        if is_game_feasible(max_colors):
            sum += game_id

    return sum


def get_power(max_dice: dict[str, int]) -> int:
    power = 1
    for dice in max_dice.values():
        power *= dice
    return power


def part2(lines: list[str]) -> int:
    power = 0
    for line in lines:
        max_colors = parse_line(line)
        power += get_power(max_colors)

    return power
