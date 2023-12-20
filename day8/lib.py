import dataclasses
from typing import Generator


@dataclasses.dataclass
class Network:
    name: str
    left: "Network"
    right: "Network"


def parse_network_line(line: str) -> tuple[str, str, str]:
    line = line.translate({ord("("): "", ord(")"): "", ord("="): ",", ord(" "): ""})
    return tuple(line.split(","))


def parse(lines: list[str]) -> tuple[str, Network]:
    lr = lines[0].strip()

    def defaultdict(d: dict, key: str):
        if key not in d:
            d[key] = Network(key, None, None)
        return d[key]

    all_nodes = dict()
    for line in lines[2:]:
        a, b, c = parse_network_line(line)

        node = defaultdict(all_nodes, a)
        node.left = defaultdict(all_nodes, b)
        node.right = defaultdict(all_nodes, c)

    return lr, all_nodes


def lr_generator(lr: str):
    while True:
        yield from lr


def part1(lines: list[str]) -> int:
    lr, network = parse(lines)
    current_node = network["AAA"]

    lr_gen = lr_generator(lr)

    count = 0
    for lr in lr_gen:
        if lr == "L":
            current_node = current_node.left
        else:
            current_node = current_node.right

        count += 1
        if current_node == network["ZZZ"]:
            break

    return count
