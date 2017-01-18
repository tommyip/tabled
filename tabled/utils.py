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
