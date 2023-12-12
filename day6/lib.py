from typing import Callable


def parse_input(lines: list[str]) -> tuple[list[int], list[int]]:
    times = tuple(int(t) for t in lines[0][9:].split(" ") if t)
    distances = tuple(int(d) for d in lines[1][9:].split(" ") if d)

    return (times, distances)


def bisect(f: Callable[[int], bool], i_min: int, i_max: int) -> int:
    while abs(i_min - i_max) > 1:
        i_mid = (i_min + i_max) // 2
        if f(i_mid):
            i_max = i_mid
        else:
            i_min = i_mid

    return i_max


def distance_by_powerup(total_race_time: int, powerup_time: int) -> int:
    return (total_race_time - powerup_time) * powerup_time


def smallest_winning_powerup(t: int, record: int):
    def is_larger_than_record(powerup_time: int) -> bool:
        return distance_by_powerup(t, powerup_time) > record

    return bisect(is_larger_than_record, i_min=0, i_max=t // 2)


def get_winning_times_count(t: int, record: int) -> int:
    powerup = smallest_winning_powerup(t, record)
    return (t + 1) - powerup * 2


def part1(lines: list[str]) -> int:
    times, distances = parse_input(lines)
    key = 1
    for t, d in zip(times, distances):
        key *= get_winning_times_count(t, d)
    return key
