"""Unit tests for Small codes mathematical and logic utilities."""

import sys
from pathlib import Path
import pytest

# Add Small codes directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "Small codes"))

from BMI import calculate_bmi, get_bmi_category
from leap_year import is_leap_year
from prime_number_checker import is_prime
from odd_even_checker import is_even


# --- BMI Tests ---
def test_calculate_bmi():
    assert round(calculate_bmi(70, 1.75), 2) == 22.86


def test_calculate_bmi_invalid_height():
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)


def test_get_bmi_category():
    assert get_bmi_category(30.0) == "Over Weight"
    assert get_bmi_category(22.0) == "Normal Weight"
    assert get_bmi_category(16.5) == "Under weight"


# --- Leap Year Tests ---
def test_is_leap_year_standard():
    assert is_leap_year(2024) is True
    assert is_leap_year(2023) is False


def test_is_leap_year_century_rules():
    assert is_leap_year(1900) is False
    assert is_leap_year(2000) is True


# --- Prime Checker Tests ---
def test_is_prime_numbers():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(25) is False
    assert is_prime(-5) is False


# --- Odd Even Checker Tests ---
def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True
