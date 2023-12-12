from dataclasses import dataclass, field


@dataclass
class Map:
    that_start: int
    this_start: int
    length: int

    def __post_init__(self):
        self.this_end = self.this_start + self.length - 1

    def in_range(self, input: int) -> int:
        return self.this_start <= input <= self.this_end

    def map(self, input: int) -> int:
        if self.in_range(input):
            return input - self.this_start + self.that_start
        return input


@dataclass
class Converter:
    maps: list[Map] = field(default_factory=list)

    def add_map(self, map: Map):
        self.maps.append(map)

    def map(self, input: int) -> int:
        for map in self.maps:
            if map.in_range(input):
                return map.map(input)
        return input


@dataclass(frozen=True)
class Parse:
    seeds: tuple[int, ...]
    stages: list[Converter]


def line_to_ints(line: str) -> tuple[int, ...]:
    return tuple(int(v) for v in line.split(" ") if v)


def parse_input(lines: list[str]) -> Parse:
    seeds = line_to_ints(lines[0].split(":")[1])

    stages = []
    converter = Converter()
    for line in lines[1:]:
        if line.endswith("map:"):
            converter = Converter()
            continue

        if line.strip() == "":
            if len(converter.maps):
                stages.append(converter)
            continue

        start, end, length = line_to_ints(line)
        converter.add_map(Map(start, end, length))
    stages.append(converter)

    return Parse(seeds, stages)


def part1(lines: list[str]) -> int:
    parse = parse_input(lines)
    locations = []
    for seed in parse.seeds:
        mapped_value = seed
        for converter in parse.stages:
            mapped_value = converter.map(mapped_value)
        locations.append(mapped_value)

    return min(locations)

