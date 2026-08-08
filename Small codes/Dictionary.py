"""Dictionary Operations and Manipulation Demo."""

from typing import Dict


def demonstrate_dictionary_basics() -> None:
    """Demonstrate dictionary initialization, insertion, updating, and iteration."""
    fruits: Dict[str, str] = {}
    fruits["Apple"] = "Red"
    fruits["Mango"] = "Yellow"
    fruits["Orange"] = "Orange"
    fruits["Pomegranate"] = "Dark Red"
    fruits["Guava"] = "Light Green"

    print("--- Fruits Color Mapping ---")
    for fruit, color in fruits.items():
        print(f"  {fruit}: {color}")

    students: Dict[str, str] = {
        "Umair": "Arshad",
        "Asad": "Arshad Pervaiz",
        "Aman": "Ullah",
        "Abdullah": "Waheed",
        "Rayyan": "Mughal",
        "Maaz": "Uddin"
    }

    students["Umair"] = "Arshad Bhai"
    print("\n--- Student Roster ---")
    for name, father_name in students.items():
        print(f"  Student: {name} | Father: {father_name}")


if __name__ == "__main__":
    demonstrate_dictionary_basics()