def parse(lines: list[str]) -> list[list[int]]:
    return [[int(d) for d in line.split()] for line in lines]


def diff(history: list[int]) -> list[int]:
    return [b - a for a, b in zip(history[:-1], history[1:])]


def get_layers(history: list[int]) -> list[list[int]]:
    layers = [history]
    layer = history
    while any(layer):
        layer = diff(layer)
        layers.append(layer)

    return layers


def predict(history: list[int]) -> int:
    layers = get_layers(history)

    next_value = 0
    for d in reversed(layers):
        next_value = next_value + d[-1]

    return next_value


def extrapolate_backwards(history: list[int]) -> int:
    layers = get_layers(history)

    next_value = 0
    for d in reversed(layers):
        next_value = d[0] - next_value

    return next_value


def part1(lines: list[str]) -> int:
    histories = parse(lines)
    return sum(predict(history) for history in histories)


def part2(lines: list[str]) -> int:
    histories = parse(lines)
    return sum(extrapolate_backwards(history) for history in histories)
