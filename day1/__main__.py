from pathlib import Path

from . import lib

with open(Path(__file__).parent.joinpath("data/input.txt"), "r", encoding="utf-8") as f:
    lines = f.read().split("\n")


sum = 0
for line in lines:
    sum += lib.first_and_last_number_as_int(line)

part1 = sum

sum = 0
for line in lines:
    value = lib.first_and_last_number2_as_int(line)
    sum += value

part2 = sum

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
