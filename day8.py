from collections import namedtuple
from collections.abc import Iterator
from pathlib import Path

Point = namedtuple("Point", ["x", "y"])


def read_input() -> list[list[str]]:
    return [
        list(line) for line in Path("inputs/day8.txt").read_text().strip().splitlines()
    ]


def find_neighbors(
    grid: list[list[str]], start: Point, antenna: str
) -> Iterator[Point]:
    for x, _ in enumerate(grid):
        for y, _ in enumerate(grid):
            cell = grid[x][y]
            if cell == ".":
                continue

            point = Point(x, y)
            if point == start:
                continue

            if cell == antenna:
                yield point


def part1() -> int:
    grid = read_input()

    anti_nodes = set()
    dimension = len(grid)

    for x, _ in enumerate(grid):
        for y, _ in enumerate(grid):
            val = grid[x][y]
            if val == ".":
                continue

            point = Point(x, y)
            # TODO:part2 keep going in this same direction until we leave the grid
            for neighbor in find_neighbors(grid, point, val):
                diff_x, diff_y = point.x - neighbor.x, point.y - neighbor.y
                anti_node = Point(point.x + diff_x, point.y + diff_y)
                # Check if this is within the bounds of the grid
                if (anti_node.x >= 0 and anti_node.x < dimension) and (
                    anti_node.y >= 0 and anti_node.y < dimension
                ):
                    anti_nodes.add(anti_node)

    return len(anti_nodes)


if __name__ == "__main__":
    print(part1())
