from collections import namedtuple
from pathlib import Path

Grid = list[list[str]]


def read_input() -> list[list[str]]:
    return [
        [char for char in line]
        for line in Path("inputs/day6.txt").read_text().strip().splitlines()
    ]


Point = namedtuple("Point", ["x", "y"])


def find_starting_position(grid: Grid) -> Point:
    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char == "^":
                return Point(x, y)
    raise ValueError("no starting pos found")


def walked_paths(grid: Grid, pos: Point) -> set[Point]:
    grid[pos.x][pos.y] = "."

    dir = 0
    dirs = (Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1))
    dimension = len(grid)
    walked = set()

    while True:
        x = pos.x + dirs[dir].x
        y = pos.y + dirs[dir].y
        if (x < 0 or x >= dimension) or (y < 0 or y >= dimension):
            break
        if grid[x][y] == ".":
            pos = Point(x, y)
            walked.add(pos)
        else:
            dir = (dir + 1) % 4
    return walked


def count_cycles(grid: Grid, pos: Point) -> int:
    dirs = (Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1))
    dimension = len(grid)

    def detect_cycle(grid: Grid, pos: Point) -> bool:
        dir = 0
        visited: set[tuple[Point, int]] = set()
        while True:
            x = pos.x + dirs[dir].x
            y = pos.y + dirs[dir].y
            if (x < 0 or x >= dimension) or (y < 0 or y >= dimension):
                return False
            if grid[x][y] == ".":
                pos = Point(x, y)
                if (pos, dir) in visited:
                    return True
                visited.add((pos, dir))
            else:
                dir = (dir + 1) % 4

    # Consider all walked paths
    cycles = 0
    for point in walked_paths(grid, pos):
        if point == pos:
            continue
        if grid[point.x][point.y] == ".":
            # Does placing a O cause a cycle
            grid[point.x][point.y] = "O"
            if detect_cycle(grid, pos):
                cycles += 1
            # Reset back to dot
            grid[point.x][point.y] = "."

    return cycles


def part1() -> int:
    grid = read_input()
    start = find_starting_position(grid)
    return len(walked_paths(grid, start))


def part2() -> int:
    grid = read_input()
    start = find_starting_position(grid)
    return count_cycles(grid, start)


if __name__ == "__main__":
    # print(part1())
    print(part2())
