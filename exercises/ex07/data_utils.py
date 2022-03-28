"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730309291"

# Define your functions below
DATA_DIRECTORY = "../../data"
DATA_FILE_PATH = f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file 
    file_handle = open(filename, "r", encoding="utf8")
    # Read that file

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of CSV line by line
    for row in csv_reader:
        result.append(row)

    # Close the file when doen to free its resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a table using just the first few rows of data."""
    result: dict[str, list[str]] = {}
    for column in table:
        list_of_items: list[str] = []
        i: int = 0
        if n > len(table[column]):
            result[column] = table[column]
        else:
            while i < n:
                list_of_items.append(table[column][i])
                i += 1
            result[column] = list_of_items
    return result 


def select(columns: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with specific selections from the original columns."""
    result: dict[str, list[str]] = {}
    for key in names:
        result[key] = columns[key]
    return result


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new table that combines data from two separate tables."""
    result: dict[str, list[str]] = {}
    for key in first:
        result[key] = first[key]
    for key in second:
        if key in result:
            result[key] += second[key]
        else:
            result[key] = second[key]
    return result


def count(given: list[str]) -> dict[str, int]:
    """Counts the number of times a value appeared in the given list."""
    result: dict[str, int] = {}
    for i in range(len(given)):
        if given[i] in result:
            result[given[i]] += 1
        else:
            result[given[i]] = 1
    return result
