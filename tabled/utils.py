"""
tabled.utils
~~~~~~~~~~~~

:synopsis: Utility functions.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

from typing import List, Text, Any


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
    """ Transform rows to columns and columns to rows.

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


def columns_width(table: List[List[Text]]) -> List[int]:
    """ Finds the width for each column in a table.

    Args:
        table: Nested list of lists that is represented as a table structure.

    Returns:
        A list of integers showing the width for each columns. The width is
        the determined by the longest text in a column.

    Example:
        >>> columns_width([['Example', 'This is very long'],
        ...                ['Short', 'word'],
        ...                ['Another long example', 'var']])
        [20, 17]
    """

    rotated_table = rotate_table(table)

    return list(map(max_width, rotated_table))


def str_list(raw_list: List[Any]) -> List[Text]:
    """ Cast all elements in a list to Text type. """

    return [str(item) for item in raw_list]


def str_nested_list(nested_raw_list: List[List[Any]]) -> List[List[Text]]:
    """ Cast all elements in a nested list to Text type. """

    return [[str(item) for item in raw_list] for raw_list in nested_raw_list]
