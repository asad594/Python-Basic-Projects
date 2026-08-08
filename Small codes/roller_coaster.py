"""Roller Coaster Ride Height and Weight Qualification Utility."""


def check_roller_coaster_eligibility(height_cm: float, weight_kg: float) -> bool:
    """Check if rider meets minimum height (120cm) and maximum weight (100kg) rules.

    Args:
        height_cm: Rider height in centimeters.
        weight_kg: Rider weight in kilograms.

    Returns:
        True if eligible, False otherwise.
    """
    return height_cm >= 120 and weight_kg <= 100


def main() -> None:
    """Run interactive Roller Coaster Qualification CLI."""
    print("Welcome to the Roller Coaster Ride!")
    try:
        height = float(input("Enter your height in cm: "))
        weight = float(input("Enter your weight in kg: "))

        if check_roller_coaster_eligibility(height, weight):
            print("🎉 Congratulations! You are eligible for the roller coaster ride.")
        else:
            print("Sorry, you are not eligible. Minimum height is 120cm and maximum weight is 100kg.")
    except ValueError:
        print("Invalid numerical input!")


if __name__ == "__main__":
    main()
