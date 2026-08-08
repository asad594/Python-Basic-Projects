"""Body Mass Index (BMI) Calculator Utility."""


def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI given weight in kg and height in meters.

    Args:
        weight: Weight in kilograms.
        height: Height in meters.

    Returns:
        Calculated BMI float.
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    return weight / (height ** 2)


def get_bmi_category(bmi: float) -> str:
    """Classify BMI score into standard health categories."""
    if bmi >= 25.0:
        return "Over Weight"
    elif bmi >= 18.5:
        return "Normal Weight"
    else:
        return "Under weight"


def main() -> None:
    """Run interactive BMI CLI."""
    try:
        height = float(input("Enter height in meters (e.g., 1.75): "))
        weight = float(input("Enter weight in kg: "))
        bmi = calculate_bmi(weight, height)
        print(f"The BMI is: {bmi:.2f}")
        print(f"Category: {get_bmi_category(bmi)}")
    except ValueError as err:
        print(f"Input Error: {err}")


if __name__ == "__main__":
    main()