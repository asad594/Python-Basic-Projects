"""Manual Loop Implementation of Min, Max, and Sum Utilities."""

from typing import List, Tuple


def calculate_sum_loop(numbers: List[int]) -> int:
    """Calculate total sum using an explicit for loop."""
    total = 0
    for num in numbers:
        total += num
    return total


def find_max_loop(numbers: List[int]) -> int:
    """Find maximum element using an explicit for loop."""
    if not numbers:
        raise ValueError("List cannot be empty.")
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def find_min_loop(numbers: List[int]) -> int:
    """Find minimum element using an explicit for loop."""
    if not numbers:
        raise ValueError("List cannot be empty.")
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val


def main() -> None:
    """Run manual loop statistics demonstration."""
    student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
    print("--- Manual Loop Score Statistics ---")
    print(f"Total Sum : {calculate_sum_loop(student_scores)}")
    print(f"Maximum   : {find_max_loop(student_scores)}")
    print(f"Minimum   : {find_min_loop(student_scores)}")


if __name__ == "__main__":
    main()
