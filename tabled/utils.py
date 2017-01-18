"""
tabled.utils
~~~~~~~~~~~~

:synopsis: Utility functions.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

from typing import List, Text


def max_width(column: List[Text]) -> int:
    """ Finds the longest string in a column and returns its length.

    Args:
        column: A list of strings represented as a column in a table.

    Returns:
        The length of the longest string.

    Example:
        >>> max_width(['example text', 'Some long lines.', 'short'])
        16
    """

    longest_string = max(column, key=len)
    return len(longest_string)


def rotate_table(table: List[List[Text]]) -> List[List[Text]]:
    """ Rotate table so that each row contains element from the same column.

    Rotate a nested list such that the columns become rows, allowing the
    maximum length of each column to be calcuated.

    Args:
        table: Nested list of lists that is represented as a table structure.

    Returns:
        A rotated table with columns as rows.

    Note:
        This operation is non directional, so applying this function twice
        would return the orginal input.

    Example:
        >>> rotate_table([['x1', 'x2', 'x3'],
        ...               ['y1', 'y2', 'y3'],
        ...               ['z1', 'z2', 'z3']])
        ... # doctest: +NORMALIZE_WHITESPACE
        [['x1', 'y1', 'z1'],
         ['x2', 'y2', 'z2'],
         ['x3', 'y3', 'z3']]
    """

    return [list(row) for row in zip(*table)]
