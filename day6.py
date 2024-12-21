from pathlib import Path


def read_input() -> list[list[str]]:
    return [
        [char for char in line]
        for line in Path("inputs/day6.txt").read_text().strip().splitlines()
    ]


def pp_grid(grid: list[list[str]]) -> None:
    for line in grid:
        print("".join(line))


def find_starting_position(grid: list[list[str]]) -> tuple[int, int]:
    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char == "^":
                return x, y
    raise ValueError("no starting pos found")


def simulate(
    grid: list[list[str]], pos: tuple[int, int], direction: str = "U"
) -> list[list[str]]:
    x, y = pos
    dimension = len(grid)
    while True:
        grid[x][y] = "X"
        if direction == "U":
            if x == 0:
                return grid
            next_tile = grid[x - 1][y]
            if next_tile == "#":
                direction = "R"
            else:
                x, y = x - 1, y
        elif direction == "R":
            if y == dimension:
                return grid
            next_tile = grid[x][y + 1]
            if next_tile == "#":
                direction = "D"
            else:
                x, y = x, y + 1
        elif direction == "D":
            if x == dimension:
                return grid
            next_tile = grid[x + 1][y]
            if next_tile == "#":
                direction = "L"
            else:
                x, y = x + 1, y
        elif direction == "L":
            if y == 0:
                return grid
            next_tile = grid[x][y - 1]
            if next_tile == "#":
                direction = "U"
            else:
                x, y = x, y - 1


def count_walked(grid: list[list[str]]) -> int:
    flattened = [char for line in grid for char in line]
    return sum([char == "X" for char in flattened])


def part1() -> int:
    grid = read_input()
    start = find_starting_position(grid)
    end = simulate(grid, start)
    return count_walked(end)


if __name__ == "__main__":
    print(part1())
