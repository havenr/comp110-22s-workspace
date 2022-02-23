"""Utilities for EX05."""

__author__ = "730309291"


def only_evens(xs: list[int]) -> list[int]:
    """Returns only even integers from list of integers."""
    i: int = 0 
    results: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            results.append(xs[i])        
        i += 1
    return results


def sub(xs: list[int], start: int, stop: int) -> list[int]:
    """When given a list and start and stop index, returns a subset of given list."""
    subset: list[int] = []
    if start < 0:
        start = 0
    if stop > len(xs):
        stop = len(xs)
    if len(xs) == 0 or start > len(xs) or stop <= 0:
        return subset
    while start < stop:
        subset.append(xs[start])
        start += 1 
    return subset 


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """When given two lists, returns both lists combined."""
    both_lists: list[int] = []
    i: int = 0
    while i < len(xs):
        both_lists.append(xs[i])
        i += 1
    i = 0
    while i < len(ys):
        both_lists.append(ys[i])
        i += 1
    return both_lists