"""Band Name Generator Utility."""


def generate_band_name(city: str, pet_name: str) -> str:
    """Combine city name and pet name to create a band name."""
    return f"{city.strip().capitalize()} {pet_name.strip().capitalize()}"


def main() -> None:
    """Run interactive Band Name Generator CLI."""
    print("Welcome to the Band Name Generator!")
    city = input("Enter the city you grew up in: ")
    pet = input("Enter the name of a pet: ")
    band_name = generate_band_name(city, pet)
    print(f"Your generated band name is: {band_name}")


if __name__ == "__main__":
    main()
