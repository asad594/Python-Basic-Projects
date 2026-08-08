"""Nested Dictionary Access and Travel Log Utility."""

from typing import Dict, List, Any


def print_travel_log(log: Dict[str, Dict[str, Any]]) -> None:
    """Format and print nested travel log dictionary data."""
    for country, details in log.items():
        print(f"\n=== {country.upper()} ===")
        print(f"Total Visits: {details.get('total_visit', 0)}")
        cities = ", ".join(details.get('total_cities', []))
        print(f"Visited Cities: {cities}")


def main() -> None:
    """Run travel log nesting demonstration."""
    travel_log: Dict[str, Dict[str, Any]] = {
        "France": {
            "total_cities": ["Paris", "Lille", "Dijon"],
            "total_visit": 12
        },
        "Germany": {
            "total_cities": ["Stuttgart", "Berlin"],
            "total_visit": 14
        },
        "Pakistan": {
            "total_cities": ["Lahore", "Islamabad"],
            "total_visit": 8
        }
    }
    print_travel_log(travel_log)


if __name__ == "__main__":
    main()