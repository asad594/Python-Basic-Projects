"""Dictionary Comprehension Demonstration Utility."""

from typing import Dict


def word_lengths(sentence: str) -> Dict[str, int]:
    """Calculate letter counts for each word in a sentence string using dictionary comprehension."""
    return {word: len(word) for word in sentence.split()}


def convert_celsius_to_fahrenheit(weather_c: Dict[str, float]) -> Dict[str, float]:
    """Convert daily temperature mapping from Celsius to Fahrenheit."""
    return {day: round((temp_c * 9 / 5) + 32, 1) for day, temp_c in weather_c.items()}


def main() -> None:
    """Run dictionary comprehension examples."""
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    print("Word Length Mapping:")
    print(word_lengths(sentence))

    weather_c = {
        "Monday": 12, "Tuesday": 14, "Wednesday": 15,
        "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24
    }
    print("\nFahrenheit Temperature Mapping:")
    print(convert_celsius_to_fahrenheit(weather_c))


if __name__ == "__main__":
    main()