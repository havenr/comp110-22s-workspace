"""Tests for Exercise 5."""

__author__ = "730309291"

from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Tests function only_evens to ensure only even integers returned."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_sub() -> None:
    """Tests functions sub to ensure start index and sublist printed, not end index."""
    xs: list[int] = [10, 20, 30, 40, 50]
    start: int = 1
    stop: int = 3
    assert sub(xs, start, stop) == [20, 30]


def test_concat() -> None:
    """Tests function concat to ensure both lists printed, second following the first."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5]
    assert concat(xs, ys) == [1, 2, 3, 4, 5]
