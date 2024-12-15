from pathlib import Path


def read_input() -> list[list[int]]:
    return [
        [int(n) for n in line.split()]
        for line in Path("inputs/day2.txt").read_text().strip().splitlines()
    ]


def criteria_a(levels: list[int]) -> bool:
    """
    The levels are either all increasing or all decreasing.
    """
    start, next, *rest = levels
    if start > next:
        # Decreasing
        for n in rest:
            if not next > n:
                return False
            next = n
    elif start < next:
        # Increasing
        for n in rest:
            if not next < n:
                return False
            next = n
    else:
        return False

    return True


def criteria_b(levels: list[int]) -> bool:
    """
    Any two adjacent levels differ by at least one and at most three.
    """
    prev, *rest = levels
    for n in rest:
        diff = abs(n - prev)
        if 1 < diff > 3:
            return False
        prev = n
    return True


def is_safe(levels: list[int]) -> bool:
    return criteria_a(levels) and criteria_b(levels)


def part1() -> int:
    return sum([is_safe(levels) for levels in read_input()])


def part2() -> int:
    safe_levels = 0

    for levels in read_input():
        print(levels)
        if is_safe(levels):
            safe_levels += 1
        else:
            # Brute force find a safe version
            for i in range(len(levels)):
                removed = levels[:i] + levels[i + 1 :]
                if is_safe(removed):
                    safe_levels += 1
                    break

    return safe_levels


if __name__ == "__main__":
    # print(part1())
    print(part2())
