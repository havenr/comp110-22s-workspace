"""Tests for EX06 Dictionary."""

__author__ = "730309291"

from dictionary import invert, favorite_colors, count


def test_invert() -> None:
    """Tests invert function to see if list is inverted."""
    x: dict[str, str] = {"apple": "cat"}
    assert invert(x) == {"cat": "apple"}


def test_favorite_colors() -> None:
    """Tests favorite colors function to see if mentioning most frequently listed color."""
    a: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_colors(a) == "blue"


def test_count() -> None:
    """Tests count function to ensure counting strings properly."""
    my_list: list[str] = ["apple", "carrot"]
    result: dict[str, int]
    assert count(my_list) == {"apple": 1, "carrot": 1}
