"""Bill Tip Split Calculator Utility."""


def calculate_tip_split(bill: float, tip_percentage: float, num_people: int) -> float:
    """Calculate the individual pay amount per person after adding percentage tip.

    Args:
        bill: Total bill amount in currency units.
        tip_percentage: Tip percentage (e.g., 10, 12, 15).
        num_people: Number of people splitting the bill.

    Returns:
        Per-person cost rounded to 2 decimal places.
    """
    if num_people <= 0:
        raise ValueError("Number of people must be greater than zero.")
    if bill < 0 or tip_percentage < 0:
        raise ValueError("Bill and tip percentage cannot be negative.")

    total_tip = bill * (tip_percentage / 100.0)
    total_bill = bill + total_tip
    return round(total_bill / num_people, 2)


def main() -> None:
    """Run interactive Tip Calculator CLI."""
    print("Welcome to the Tip Calculator!")
    try:
        bill = float(input("What was the total bill? $"))
        tip = float(input("How much tip percentage would you like to give? (e.g. 10, 12, 15): "))
        people = int(input("How many people to split the bill?: "))

        amount_per_person = calculate_tip_split(bill, tip, people)
        print(f"\nEach person should pay: ${amount_per_person:.2f}")
    except ValueError as err:
        print(f"Input Error: {err}")


if __name__ == "__main__":
    main()
