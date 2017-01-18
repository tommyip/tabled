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
        string: A text value to be padded with spaces.
        width: The width of the string container.

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
        string: A text value to be padded with spaces.
        width: The width of the string container.

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


def left_right_pad(string: Text, width: int) -> Text:
    """ Insert padding in both side of a string inside a container.

    Note:
        If the size of the padding cannot be divided equally by 2, the right
        side would be allocated with more spaces.

    Args:
        string: A text value to be padded with spaces.
        width: The width of the string container.

    Returns:
        A string `width` wide with `string` aligned center.

    Example:
        >>> left_right_pad('tableD', 11)
        '  tableD   '
    """

    string_length = len(string)
    pad_amount = width - string_length

    if pad_amount < 0:
        # Container too narrow
        raise ValueError('The input string is longer than the allowed width.')

    left_padded = left_pad(string, (pad_amount // 2) + string_length)
    return right_pad(left_padded, width)
