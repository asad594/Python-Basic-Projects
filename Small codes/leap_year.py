"""Leap Year Evaluator Utility."""


def is_leap_year(year: int) -> bool:
    """Determine whether a given calendar year is a leap year.

    Args:
        year: The target integer calendar year.

    Returns:
        True if year is a leap year, False otherwise.
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def main() -> None:
    """Run interactive Leap Year CLI."""
    try:
        year = int(input("Enter the year: "))
        if is_leap_year(year):
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is Not a Leap Year.")
    except ValueError:
        print("Invalid year input!")


if __name__ == "__main__":
    main()