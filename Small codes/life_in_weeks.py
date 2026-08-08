"""Life in Weeks Calculator Utility."""


def calculate_weeks_remaining(age: int, target_age: int = 90) -> int:
    """Calculate remaining life duration in weeks assuming a target age.

    Args:
        age: Current age in years.
        target_age: Goal total age horizon (default 90).

    Returns:
        Remaining weeks integer.
    """
    years_remaining = max(0, target_age - age)
    return years_remaining * 52


def main() -> None:
    """Run interactive Life in Weeks CLI."""
    try:
        current_age = int(input("Enter your current age in years: "))
        weeks = calculate_weeks_remaining(current_age)
        print(f"You have approximately {weeks} weeks left until age 90.")
    except ValueError:
        print("Invalid age input!")


if __name__ == "__main__":
    main()