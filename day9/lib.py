def parse(lines: list[str]) -> list[list[int]]:
    return [[int(d) for d in line.split()] for line in lines]


def diff(history: list[int]) -> list[int]:
    return [b - a for a, b in zip(history[:-1], history[1:])]


def predict(history: list[int]) -> int:
    layers = [history]
    layer = history
    while any(layer):
        layer = diff(layer)
        layers.append(layer)

    next_value = 0
    for d in reversed(layers):
        next_value = next_value + d[-1]

    return next_value


def part1(lines: list[str]) -> int:
    histories = parse(lines)
    return sum(predict(history) for history in histories)
