from collections import deque
from itertools import zip_longest
from pathlib import Path
from typing import cast


def read_input() -> list[int]:
    return [int(n) for n in Path("inputs/day9.txt").read_text().strip()]


def disk_map(parsed: list[int]) -> list[int | str]:
    blocks = parsed[::2]
    free_spaces = parsed[1::2]
    disk_map: list[int | str] = []
    for index, (block, free_space) in enumerate(zip_longest(blocks, free_spaces)):
        if block is not None:
            for _ in range(block):
                disk_map.append(index)
        if free_space is not None:
            for _ in range(free_space):
                disk_map.append(".")
    return disk_map


def move_blocks(disk_map: list[int | str]) -> list[int | str]:
    free_index: deque[int] = deque()
    block_index: deque[int] = deque()

    for index, block in enumerate(disk_map):
        if block == ".":
            free_index.append(index)
        else:
            block_index.append(index)

    while True:
        free_block = block_index.pop()
        free_space = free_index.popleft()

        if free_space > free_block:
            return disk_map

        disk_map[free_block], disk_map[free_space] = (
            disk_map[free_space],
            disk_map[free_block],
        )


def check_sum(disk_map: list[int | str]) -> int:
    total = 0
    for index, num in enumerate(disk_map):
        if num == ".":
            return total
        else:
            total += index * cast(int, num)
    raise Exception("impossible state")


def part1() -> int:
    parsed = read_input()
    mapped = disk_map(parsed)
    balanced = move_blocks(mapped)
    return check_sum(balanced)


if __name__ == "__main__":
    print(part1())
