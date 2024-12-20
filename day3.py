import re
from collections.abc import Iterator
from operator import mul
from pathlib import Path


def read_input() -> str:
    return Path("inputs/day3.txt").read_text().strip()


def parse(input: str) -> Iterator[tuple[int, int]]:
    for match in re.finditer(r"mul\((\d+),(\d+)\)", input):
        x, y = match.groups()
        yield (int(x), int(y))


def strip_donts(input: str) -> Iterator[str]:
    # Split on every don't() parse until next do (if exists)
    for part in input.split("don't()"):
        next_do = part.find("do()")
        if next_do != -1:
            yield part[next_do:]


def part1() -> int:
    return sum([mul(*vals) for vals in parse(read_input())])


def part2() -> int:
    stripped = "".join(strip_donts(read_input()))
    return sum([mul(*vals) for vals in parse(stripped)])


if __name__ == "__main__":
    print(part1())
    print(part2())
