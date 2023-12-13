from dataclasses import dataclass, field


@dataclass
class Map:
    this_start: int
    that_start: int
    length: int

    def __post_init__(self):
        self.this_end = self.this_start + self.length - 1
        self.that_end = self.that_start + self.length - 1

    def in_range(self, input: int) -> int:
        return self.this_start <= input <= self.this_end

    def map(self, input: int) -> int:
        if self.in_range(input):
            return input - self.this_start + self.that_start
        return input

    def __hash__(self) -> int:
        return hash((self.that_start, self.this_start, self.length))


@dataclass
class Converter:
    maps: set[Map] = field(default_factory=set)

    def add_map(self, map: Map):
        self.maps.add(map)

    def map(self, input: int) -> int:
        for map in self.maps:
            if map.in_range(input):
                return map.map(input)
        return input

    def __repr__(self) -> str:
        s = ""
        for map in sorted(self.maps, key=lambda map: map.this_start):
            s += f"{map.this_start}:{map.this_end + 1}->{map.that_start}:{map.that_end + 1}, "
        s = s.rstrip()
        s = s.rstrip(",")
        return f"<{s}>"


@dataclass(frozen=True)
class Parse:
    seeds: tuple[int, ...]
    stages: list[Converter]

    def seed_location(self, seed: int) -> int:
        mapped_value = seed
        for converter in self.stages:
            mapped_value = converter.map(mapped_value)
        return mapped_value


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

        to, from_, length = line_to_ints(line)
        converter.add_map(Map(from_, to, length))
    stages.append(converter)

    return Parse(seeds, stages)


def part1(lines: list[str]) -> int:
    parse = parse_input(lines)
    locations = []
    for seed in parse.seeds:
        locations.append(parse.seed_location(seed))

    return min(locations)


# https://stackoverflow.com/a/312464/4713758
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def part2(lines: list[str]) -> int:
    parse = parse_input(lines)
    locations = []
    for first_seed, length in chunks(parse.seeds, 2):
        last_seed = first_seed + length - 1
        locations.append(first_seed)
        locations.append(last_seed)

    return min(locations)
