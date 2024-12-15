from collections import Counter
from pathlib import Path


def read_input() -> list[list[int]]:
    return [
        [int(n) for n in line.split()]
        for line in Path("inputs/day1.txt").read_text().strip().splitlines()
    ]


def part1() -> int:
    x, y = zip(*read_input(), strict=False)
    sorted_x, sorted_y = sorted(x), sorted(y)
    return sum((abs(int(x) - int(y)) for x, y in zip(sorted_x, sorted_y, strict=False)))


def part2() -> int:
    x, y = zip(*read_input(), strict=False)
    freq_y = Counter(y)
    return sum(int(n) * int(freq_y[n]) for n in x)


if __name__ == "__main__":
    print(part1())
    # print(part2())
