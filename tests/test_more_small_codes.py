"""Additional unit tests for Small codes utility functions."""

import sys
from pathlib import Path
import pytest

# Add Small codes directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "Small codes"))

from Fizz_Buzz_game import evaluate_fizz_buzz
from Grading_system import calculate_grade
from tip_calculatr import calculate_tip_split
from band_name_generator import generate_band_name
from life_in_weeks import calculate_weeks_remaining


def test_fizz_buzz():
    assert evaluate_fizz_buzz(15) == "FizzBuzz"
    assert evaluate_fizz_buzz(9) == "Fizz"
    assert evaluate_fizz_buzz(10) == "Buzz"
    assert evaluate_fizz_buzz(7) == "7"


def test_grading_system():
    assert calculate_grade(95) == "Outstanding"
    assert calculate_grade(85) == "Exceeds Expectations"
    assert calculate_grade(75) == "Acceptable"
    assert calculate_grade(50) == "Fail"


def test_tip_split():
    assert calculate_tip_split(100.0, 10.0, 2) == 55.0
    assert calculate_tip_split(150.0, 20.0, 5) == 36.0


def test_tip_split_invalid_people():
    with pytest.raises(ValueError):
        calculate_tip_split(100.0, 10.0, 0)


def test_band_name_generator():
    assert generate_band_name("london", "dog") == "London Dog"


def test_weeks_remaining():
    assert calculate_weeks_remaining(50, 90) == 2080
    assert calculate_weeks_remaining(90, 90) == 0
