import collections
import itertools
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import TypeVar

T = TypeVar("T")  # Define type variable "T"


def read_input() -> list[str]:
    return Path("inputs/day7.txt").read_text().strip().splitlines()


def parse_input(input: list[str]) -> Iterator[tuple[int, list[int]]]:
    for line in input:
        left, right = line.split(":")
        yield (int(left), [int(n) for n in right.split()])


def take(n: int, iterable: Iterable[T]) -> list[T]:
    "Return first n items of the iterable as a list."
    return list(itertools.islice(iterable, n))


def eval_expression(nums: list[int], operators: tuple[str, ...]) -> int | None:
    result, *rest = nums
    num_deque = collections.deque(rest)
    operator_deque = collections.deque(operators)
    while True:
        try:
            operator = operator_deque.popleft()
        except IndexError:
            return result
        else:
            rhs = num_deque.popleft()
            if operator == "*":
                result *= rhs
            elif operator == "+":
                result += rhs
            elif operator == "||":
                result = int(str(result) + str(rhs))

    return result


def passes_test(
    target: int, nums: list[int], operators: tuple[str, ...] = ("*", "+")
) -> bool:
    for combo in itertools.product(operators, repeat=len(nums) - 1):
        result = eval_expression(nums, combo)
        if result == target:
            return True
    return False


def part1() -> int:
    parsed = parse_input(read_input())
    return sum([target for target, nums in parsed if passes_test(target, nums)])


def part2() -> int:
    parsed = parse_input(read_input())
    return sum(
        [
            target
            for target, nums in parsed
            if passes_test(target, nums, operators=("*", "+", "||"))
        ]
    )


if __name__ == "__main__":
    # print(part1())
    print(part2())
