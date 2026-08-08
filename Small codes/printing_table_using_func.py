"""Multiplication Table Printing Functions Utility."""

from typing import List, Tuple


def generate_multiplication_table(number: int, end_range: int = 10) -> List[Tuple[int, int, int]]:
    """Generate multiplication table tuples of (number, multiplier, product).

    Args:
        number: Target multiplication base integer.
        end_range: Maximum multiplier limit (default 10).

    Returns:
        List of (number, i, number * i) tuples.
    """
    return [(number, i, number * i) for i in range(1, end_range + 1)]


def main() -> None:
    """Run interactive Multiplication Table CLI."""
    try:
        num = int(input("Enter number to generate multiplication table: "))
        limit = int(input("Enter table multiplier limit (e.g. 10): "))

        table = generate_multiplication_table(num, limit)
        print(f"\n--- Multiplication Table for {num} ---")
        for base, i, product in table:
            print(f"  {base} x {i:02d} = {product}")
    except ValueError:
        print("Invalid integer input!")


if __name__ == "__main__":
    main()