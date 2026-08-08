"""Odd and Even Number Classifier Utility."""


def is_even(number: int) -> bool:
    """Check if an integer is even."""
    return number % 2 == 0


def main() -> None:
    """Run interactive Odd/Even CLI."""
    print("Welcome to the Even and Odd Number Checker!")
    try:
        number = int(input("Enter a number: "))
        if is_even(number):
            print(f"{number} is an Even number.")
        else:
            print(f"{number} is an Odd number.")
    except ValueError:
        print("Invalid integer input!")


if __name__ == "__main__":
    main()
