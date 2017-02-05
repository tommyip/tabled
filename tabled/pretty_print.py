"""
tabled.pretty_print
~~~~~~~~~~~~~~~~~~~

:synopsis: Pretty printing engine for tableD.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

from typing import Dict, List, Text

from .style_templates import get_style
from .utils import columns_width


def left_pad(string: Text, width: int) -> Text:
    """ Insert spaces to the left of a string to fit into a container.

    Args:
        string: A text value to be padded with spaces.
        width: The width of the string container.

    Returns:
        A string aligned right in a container.

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
    """ Insert spaces to the right of a string to fit into a container.

    Args:
        string: A text value to be padded with spaces.
        width: The width of the string container.

    Returns:
        A string aligned left in a container.

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
    """ Insert spaces to both sides of a string to fit into a container.

    Note:
        The right side of the string would be allocated more spaces if the
        amount of blank spaces cannot be divided equally by 2.

    Args:
        string: A text value to be padded with spaces.
        width: The width of the string container.

    Returns:
        A string aligned center in a container.

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


def pad(string: Text,
        width: int,
        align: Text = 'left',
        margin: int = 1) -> Text:
    """ Pad and align a string in a container.

    Args:
        string: Input text to be padded and aligned.
        width: The width of the container.
        align: Left, center or right alignment.
        margin: Margin width between the string and the side wall.

    Returns:
        A string padded and aligned in a container.

    Example:
        >>> pad('library', 13, 'left')
        ' library     '
    """

    width_no_margin = width - (margin * 2)

    # Case/switch hack to reduce if/elif cluster.
    pad_string = {
        'left': right_pad,
        'right': left_pad,
        'center': left_right_pad
    }

    padded = pad_string[align](string, width_no_margin)

    return left_right_pad(padded, len(padded) + (margin * 2))


def construct_row(row: List[Text],
                  widths: List[int],
                  delimiters: Dict[str, Text],
                  align: Text = 'left',
                  margin: int = 1) -> Text:
    """ Render a table row.

    Args:
        row: A row of string, each is a cell of their columns.
        widths: A list of column widths.
        delimiter: A dictionary of column dividers.
        align: Left, center or right alignment of each cell.
        margin: Margin width between the string and the side wall.

    Returns:
        A string containing a print ready row.

    Example:
        >>> construct_row(['Some cell content', 'word', '1'], [22, 6, 7],
        ...               {'left': '|', 'right': '|', 'connector': '|'})
        '| Some cell content    | word | 1     |'
    """

    output = '{left_wall}{columns}{right_wall}'

    padded_row = [pad(*cell_n_width, align=align, margin=margin)
                  for cell_n_width in zip(row, widths)]

    return output.format(
        left_wall=delimiters['left'],
        columns=delimiters['connector'].join(padded_row),
        right_wall=delimiters['right']
    )


def generate_table(headings: List[Text],
                   table: List[List[Text]],
                   style: str = 'default') -> Text:
    """ This is where the magic happens!

    Args:
        headings: A list of text containing the headings.
        table: Cells data in a nested list of list structure.
        style: Style of formatting in the table.

    Returns:
        A string with formatting ready for output.

    Example:
        >>> table = [['1', '1'],
        ...          ['2', '4'],
        ...          ['3', '9']]
        >>> print(generate_table(['x', 'f(x) = x^2'], table))
        +---+------------+
        | x | f(x) = x^2 |
        +---+------------+
        | 1 | 1          |
        | 2 | 4          |
        | 3 | 9          |
        +---+------------+
    """

    styling = get_style(style)

    widths = [(width + 2) for width in columns_width([headings] + table)]

    divider = [''.join(styling['raw']['horizontal']) * width
               for width in widths]

    rows = [
        # Top border
        construct_row(divider, widths,
                      styling['top_border'], margin=0),

        # Headings
        construct_row(headings, widths, styling['row']),

        # Heading/body divider
        construct_row(divider, widths,
                      styling['divider'], margin=0),

        # Actual table body
        '\n'.join([construct_row(row, widths, styling['row'])
                   for row in table]),

        # Bottom border
        construct_row(divider, widths,
                      styling['bottom_border'], margin=0)
    ]

    return '\n'.join(rows)
