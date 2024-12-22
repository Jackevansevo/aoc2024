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


def has_free_space(disk_map: list[int | str]) -> bool:
    """
    Returns True if any disk block encountered after free space
    """
    free_space = False
    for char in disk_map:
        if char == ".":
            free_space = True
        else:
            if free_space:
                return True
    return False


def move_blocks(disk_map: list[int | str]) -> list[int | str]:
    limit = len(disk_map)
    end_block_index = 1
    free_space_index = 0

    while True:
        # We can probably optimise this to only check from a starting point
        if not has_free_space(disk_map):
            return disk_map

        disk_map[::-1]

        def find_end_block(start: int) -> int:
            for index in range(abs(start), limit):
                if disk_map[-index] == ".":
                    continue
                return -index
            raise Exception("Impossible state")

        def leftmost_free_space(start: int) -> int:
            for index in range(start, limit):
                if disk_map[index] == ".":
                    return index
                continue
            raise Exception("Impossible state")

        end_block_index = find_end_block(start=end_block_index)
        free_space_index = leftmost_free_space(start=free_space_index)

        # Swap
        disk_map[end_block_index], disk_map[free_space_index] = (
            disk_map[free_space_index],
            disk_map[end_block_index],
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
