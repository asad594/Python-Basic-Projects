"""Unit tests for Automatic Password Generator."""

import sys
from pathlib import Path

# Add project subfolder to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "Automatic Password generator"))

from main import generate_password, LETTERS, NUMBERS, SYMBOLS


def test_password_length():
    """Verify total length matches sum of specified character types."""
    password = generate_password(5, 3, 2)
    assert len(password) == 10


def test_password_zero_counts():
    """Verify empty counts produce an empty string."""
    password = generate_password(0, 0, 0)
    assert password == ""


def test_password_character_sets():
    """Verify password only contains characters from allowed sets."""
    password = generate_password(10, 5, 5)
    allowed_set = set(LETTERS + NUMBERS + SYMBOLS)
    assert all(c in allowed_set for c in password)
