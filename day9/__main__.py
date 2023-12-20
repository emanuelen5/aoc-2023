from pathlib import Path

from . import lib

with open(Path(__file__).parent.joinpath("data/input.txt"), "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

part1 = None
part2 = None

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
