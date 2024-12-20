from pathlib import Path
from typing import cast

import numpy as np


def read_input() -> list[str]:
    return Path("inputs/day4.txt").read_text().strip().splitlines()


def diagonal_lines(grid: np.ndarray) -> list[list[str]]:
    cols, rows = grid.shape
    diagonals = []
    for i in range(-(cols), cols):
        diagonals.append(cast(list[str], grid.diagonal(i).tolist()))

    flipped = np.fliplr(grid)
    for i in range(-(cols), cols):
        diagonals.append(cast(list[str], flipped.diagonal(i).tolist()))

    return diagonals


def part1() -> int:
    grid = np.array([list(row) for row in read_input()])
    rows = cast(list[list[str]], grid.tolist())
    cols = cast(list[list[str]], grid.T.tolist())
    diagonals = diagonal_lines(grid)
    all = rows + cols + diagonals
    joined = ["".join(line) for line in all]
    return sum([line.count("XMAS") + line.count("SAMX") for line in joined])


def check_xmas(grid: list[list[str]], point: tuple[int, int]) -> bool:
    x, y = point
    a, b = grid[x - 1][y - 1], grid[x - 1][y + 1]
    c, d = grid[x + 1][y - 1], grid[x + 1][y + 1]
    return (a == "M" and d == "S" or a == "S" and d == "M") and (
        b == "M" and c == "S" or b == "S" and c == "M"
    )


def find_a_points(grid: list[list[str]]) -> list[tuple[int, int]]:
    points = []
    max_bound = len(grid) - 1
    for x, row in enumerate(grid):
        if x == 0 or x >= max_bound:
            continue
        for y, letter in enumerate(row):
            if y == 0 or y >= max_bound:
                continue
            if letter == "A":
                points.append((x, y))
    return points


def part2() -> int:
    grid = [list(row) for row in read_input()]
    return sum([check_xmas(grid, point) for point in find_a_points(grid)])


if __name__ == "__main__":
    print(part1())
    print(part2())
