"""Forward and Reverse Multiplication Table Utility."""

from typing import List, Tuple


def generate_reverse_table(number: int, start: int = 20) -> List[Tuple[int, int, int]]:
    """Generate reverse multiplication table tuples from start down to 1."""
    return [(number, i, number * i) for i in range(start, 0, -1)]


def main() -> None:
    """Run forward and reverse multiplication table CLI."""
    try:
        number = int(input("Enter number for forward & reverse tables: "))

        print(f"\n--- Forward Table for {number} (1 to 20) ---")
        for i in range(1, 21):
            print(f"  {number} x {i:02d} = {number * i}")

        print(f"\n--- Reverse Table for {number} (20 down to 1) ---")
        for base, i, product in generate_reverse_table(number, 20):
            print(f"  {base} x {i:02d} = {product}")
    except ValueError:
        print("Invalid integer input!")


if __name__ == "__main__":
    main()
