from pathlib import Path
from typing import TypeVar

T = TypeVar("T")  # Define type variable "T"


def read_input() -> str:
    return Path("inputs/day5.txt").read_text().strip()


def parse_input(input: str) -> tuple[list[list[int]], list[list[int]]]:
    ordering_rules, updates = input.split("\n\n")
    parsed_ordering_rules = [
        [int(x) for x in rule.split("|")] for rule in ordering_rules.splitlines()
    ]
    parsed_updates = [
        [int(x) for x in update.split(",")] for update in updates.splitlines()
    ]
    return parsed_ordering_rules, parsed_updates


def is_correct(update: list[int], ordering_rules: list[list[int]]) -> bool:
    for index, num in enumerate(update):
        remaining = update[index + 1 :]
        # Find exceptions to the rule
        for rule in ordering_rules:
            first, second = rule
            if second == num and first in remaining:
                return False
    return True


def get_middle(lst: list[T]) -> T:
    i = (len(lst) - 1) // 2
    return lst[i]


def part1() -> int:
    ordering_rules, updates = parse_input(read_input())
    valid_updates = [update for update in updates if is_correct(update, ordering_rules)]
    return sum([get_middle(update) for update in valid_updates])


def passes_rule(
    update: list[int], rule: list[int]
) -> tuple[bool, tuple[int, int] | None]:
    first, second = rule
    if first not in update or second not in update:
        return True, None

    first_pos, second_pos = update.index(first), update.index(second)
    if first_pos > second_pos:
        return False, (first_pos, second_pos)

    return True, None


def reorder_incorrect(update: list[int], ordering_rules: list[list[int]]) -> list[int]:
    for rule in ordering_rules:
        passed, indexes = passes_rule(update, rule)
        if not passed and indexes is not None:
            first_pos, second_pos = indexes
            update[first_pos], update[second_pos] = (
                update[second_pos],
                update[first_pos],
            )
            return reorder_incorrect(update, ordering_rules)
    return update


def part2() -> int:
    ordering_rules, updates = parse_input(read_input())
    new = []
    for update in updates:
        if not is_correct(update, ordering_rules):
            new.append(reorder_incorrect(update, ordering_rules))
    return sum([get_middle(update) for update in new])


if __name__ == "__main__":
    print(part1())
    print(part2())
