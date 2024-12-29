from functools import cache, partial
from pathlib import Path


def read_input() -> list[int]:
    return [int(n) for n in Path("inputs/day11.txt").read_text().strip().split()]


@cache
def simulate(stone: int, generation: int = 25) -> int:
    """
    Simulate the total number of stones produces
    """
    # Base case (we finished the simulation)
    if generation == 0:
        return 1

    if stone == 0:
        return simulate(1, generation - 1)

    s = str(stone)
    _l = len(s)

    if _l % 2 == 0:
        half = _l // 2
        return simulate(int(s[:half]), generation - 1) + simulate(
            int(s[half:]), generation - 1
        )

    return simulate(stone * 2024, generation - 1)


def part1() -> int:
    stones = read_input()
    return sum(map(simulate, stones))


def part2() -> int:
    stones = read_input()
    return sum(map(partial(simulate, generation=75), stones))


if __name__ == "__main__":
    print(part1())
    print(part2())
