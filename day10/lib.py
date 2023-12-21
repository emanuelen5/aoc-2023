import enum

map_t = list[str]
pos_t = tuple[int, int]


class Dir(enum.Enum):
    up = (-1, 0)
    down = (1, 0)
    right = (0, 1)
    left = (0, -1)

    def __repr__(self) -> str:
        return self.name


move_t = tuple[pos_t, Dir]


def walk(move: move_t) -> move_t:
    pos, dir = move
    return tuple(a + b for a, b in zip(pos, dir.value)), dir


valid_pipe_entries: dict[move_t, Dir] = {
    ("J", Dir.right): Dir.up,
    ("J", Dir.down): Dir.left,
    ("F", Dir.up): Dir.right,
    ("F", Dir.left): Dir.down,
    ("|", Dir.up): Dir.up,
    ("|", Dir.down): Dir.down,
    ("-", Dir.left): Dir.left,
    ("-", Dir.right): Dir.right,
    ("L", Dir.left): Dir.up,
    ("L", Dir.down): Dir.right,
    ("7", Dir.right): Dir.down,
    ("7", Dir.up): Dir.left,
}


class MoveException(ValueError):
    pass


class FinishedLoop(ValueError):
    pass


def turn(tile: str, previous_dir: Dir) -> Dir:
    tile_move = (tile, previous_dir)
    if tile == "S":
        raise FinishedLoop()

    if tile_move not in valid_pipe_entries:
        raise MoveException(f"Cannot move to {tile=} with direction"
                            f" {previous_dir}")

    return valid_pipe_entries[tile_move]


def forward(map: map_t, move: move_t) -> move_t:
    # move_dir(pos, travel_dir)
    pos, dir = move
    row, col = pos
    tile = map[row][col]
    next_dir = turn(tile, dir)
    next_move = (pos, next_dir)
    return walk(next_move)


def pad(map: map_t) -> map_t:
    cols = len(map[0]) + 2
    return ["." * cols] + ["." + row + "." for row in map] + ["." * cols]


def find_start(map: map_t) -> pos_t:
    not_found = -1
    for row, line in enumerate(map):
        col = line.find("S")
        if col != not_found:
            return (row, col)


def start_seed(map: map_t) -> list[tuple[move_t]]:
    start_pos = find_start(map)
    seeds = []
    for dir in Dir:
        start_move = (start_pos, dir)
        move = walk(move=start_move)
        try:
            forward(map, move)
        except MoveException as e:
            continue
        seeds.append(move)

    return seeds


def part1(map: map_t) -> int:
    max_distance = 0
    for start in start_seed(map):
        move = start
        distance = 1
        try:
            while True:
                move = forward(map, move)
                distance += 1
        except MoveException:
            continue
        except FinishedLoop:
            max_distance = max(max_distance, distance)
    return max_distance // 2
