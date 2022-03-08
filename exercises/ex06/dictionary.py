"""EX06 Dictionary."""

__author__ = "730309291"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts key-value pairs of given dictionary."""
    y: dict[str, str] = dict() 
    for key in x:
        value: str = x[key]
        if value in y:
            raise KeyError("Cannot use this key!")
        else:
            y[value] = key
    return y


def favorite_color(a: dict[str, str]) -> str:
    """Counts and returns most frequently mentioned color."""
    b: dict[str, int] = {}
    for key in a:
        color = a[key]
        if color in b:
            b[color] += 1
        else:
            b[color] = 1
    most_freq: str = ""
    h: int = 0 
    for color in b:
        if b[color] > h:
            h = b[color]
            most_freq = color
    return most_freq


def count(my_list: list[str]) -> dict[str, int]:
    """Counts number of mentions of certain strings in a list."""
    result: dict[str, int] = {}
    for item in my_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
