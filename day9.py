from collections import deque
from itertools import groupby, zip_longest
from pathlib import Path
from typing import NamedTuple, cast

Index = tuple[int, int]


def read_input() -> list[int]:
    return [int(n) for n in Path("inputs/day9.txt").read_text().strip()]


def disk_map(parsed: list[int]) -> list[int | str]:
    blocks = parsed[::2]
    free_spaces = parsed[1::2]
    disk: list[int | str] = []
    for index, (block, free_space) in enumerate(zip_longest(blocks, free_spaces)):
        if block is not None:
            for _ in range(block):
                disk.append(index)
        if free_space is not None:
            for _ in range(free_space):
                disk.append(".")
    return disk


def move_blocks(disk: list[int | str]) -> list[int | str]:
    space_index: deque[int] = deque()
    block_index: deque[int] = deque()

    for index, block in enumerate(disk):
        if block == ".":
            space_index.append(index)
        else:
            block_index.append(index)

    while True:
        free_block = block_index.pop()
        free_space = space_index.popleft()

        if free_space > free_block:
            return disk

        disk[free_block], disk[free_space] = (
            disk[free_space],
            disk[free_block],
        )


class Block(NamedTuple):
    pos: int
    size: int


def move_files(disk: list[int | str]) -> list[int | str]:
    spaces: list[Block] = []
    blocks: deque[Block] = deque()

    index = 0
    for char, group in groupby(disk):
        size = len(list(group))
        if char == ".":
            spaces.append(Block(index, size))
        else:
            blocks.append(Block(index, size))
        index += size

    def find_space(block: Block) -> tuple[int, Block] | None:
        """
        Return index, and size of smallest possible fitting space
        """
        for index, space in enumerate(spaces):
            if space.pos > block.pos:
                continue
            if space.size >= block.size:
                return index, space
        return None

    while True:
        try:
            block = blocks.pop()
        except IndexError:
            break

        found_space = find_space(block)
        if found_space is None:
            continue

        index, space = found_space

        (
            disk[space.pos : space.pos + block.size],
            disk[block.pos : block.pos + block.size],
        ) = (
            disk[block.pos : block.pos + block.size],
            disk[space.pos : space.pos + block.size],
        )

        # Re-index any remaining free space
        if space.size > block.size:
            spaces[index] = Block(space.pos + block.size, space.size - block.size)
        else:
            del spaces[index]

    return disk


def check_sum(disk: list[int | str]) -> int:
    total = 0
    for index, num in enumerate(disk):
        if num == ".":
            continue
        else:
            total += index * cast(int, num)
    return total


def part1() -> int:
    return check_sum(move_blocks(disk_map(read_input())))


def part2() -> int:
    return check_sum(move_files(disk_map(read_input())))


if __name__ == "__main__":
    # print(part1())
    x = move_files(disk_map([int(n) for n in "2333133121414131402"]))
    assert check_sum(x) == 2858  # Check test case
    print(part2())
