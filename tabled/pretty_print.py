"""
tabled.pretty_print
~~~~~~~~~~~~~~~~~~~

:synopsis: Pretty printing engine for tableD.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

from typing import Text


def left_pad(string: Text, width: int) -> Text:
    """ Left pad a string in a container.

    Args:
        string: A text value to be padded with space.
        width: The width of the string container

    Returns:
        A string `width` wide with `string` aligned right.

    Example:
        >>> left_pad('tableD', 10)
        '    tableD'
    """

    pad_amount = width - len(string)

    if pad_amount < 0:
        # Container too narrow
        raise ValueError('The input string is longer than the allowed width.')

    return "{}{}".format(" " * pad_amount, string)


def right_pad(string: Text, width: int) -> Text:
    """ Right pad a string in a container.

    Args:
        string: A text value to be padded with space.
        width: The width of the string container

    Returns:
        A string `width` wide with `string` aligned left.

    Example:
        >>> right_pad('tableD', 10)
        'tableD    '
    """

    pad_amount = width - len(string)

    if pad_amount < 0:
        # Container too narrow
        raise ValueError('The input string is longer than the allowed width.')

    return "{}{}".format(string, " " * pad_amount)
