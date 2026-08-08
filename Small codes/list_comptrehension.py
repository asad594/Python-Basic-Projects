"""List Comprehension Demonstration Utility."""

from typing import List


def filter_even_numbers_from_strings(str_list: List[str]) -> List[int]:
    """Parse string list to integers and return list of even numbers."""
    integers = [int(x) for x in str_list]
    return [n for n in integers if n % 2 == 0]


def square_numbers(numbers: List[int]) -> List[int]:
    """Return list of squared integers."""
    return [n * n for n in numbers]


def main() -> None:
    """Run list comprehension examples."""
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    print(f"Original: {numbers}")
    print(f"Squared:  {square_numbers(numbers)}")

    raw_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
    print(f"\nFiltered Evens: {filter_even_numbers_from_strings(raw_strings)}")


if __name__ == "__main__":
    main()