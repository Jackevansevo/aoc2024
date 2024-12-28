from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path
from pprint import pprint  # noqa
from typing import NamedTuple, Self

Grid = list[list[int]]


class Point(NamedTuple):
    x: int
    y: int


@dataclass
class Tree:
    node: Point
    children: list[Self] = field(default_factory=list)

    @property
    def leaf_nodes(self: Self) -> Iterator[Point]:
        for child in self.children:
            if not child.children:
                yield child.node
            yield from child.leaf_nodes


def read_input() -> Grid:
    return [
        [int(n) for n in line]
        for line in Path("inputs/day10.txt").read_text().strip().splitlines()
    ]


def get_neighbors(point: Point, grid: Grid) -> list[Point]:
    return [
        Point(point.x - 1, point.y),
        Point(point.x + 1, point.y),
        Point(point.x, point.y - 1),
        Point(point.x, point.y + 1),
    ]


def possible_paths(point: Point, grid: Grid) -> Iterator[Point]:
    height = int(grid[point.x][point.y])
    for n in get_neighbors(point, grid):
        # Bounds check
        if n.x >= 0 and n.y >= 0 and n.x < len(grid) and n.y < len(grid):
            # Height check
            if grid[n.x][n.y] == height + 1:
                yield n


def traverse(tree: Tree, grid: Grid) -> Tree:
    children = [traverse(Tree(node=n), grid) for n in possible_paths(tree.node, grid)]
    return Tree(node=tree.node, children=children)


def part1() -> int:
    grid = read_input()
    trailheads = []
    for x, line in enumerate(grid):
        for y, num in enumerate(line):
            if num == 0:
                trailheads.append(Point(x, y))

    scores = []
    for point in trailheads:
        tree = traverse(Tree(point), grid)
        scores.append(len(set([n for n in tree.leaf_nodes if grid[n.x][n.y] == 9])))

    return sum(scores)


if __name__ == "__main__":
    print(part1())
