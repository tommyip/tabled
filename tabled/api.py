"""
tabled.api
~~~~~~~~~~

:synopsis: Main interface for tabled.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

from typing import Any, List, Optional, Text

from .tabled import TableD


def new(headings: Optional[List[Any]] = None,
        data: Optional[List[List[Any]]] = None,
        style: Text = 'default',
        align: Text = None,
        device: Text = 'stdout',
        dataframe=None) -> TableD:  # mypy: ignore
    """ Creates a new TableD object. This should be used instead of calling
    TableD's __init__() directly.

    Args:
        headings: A list of column headings.
        data: Nested list of lists of cell contents.
        style: Style of pretty printer.
        align: Align cell content to either left, center or right. Default to
               setting specified in style.
        device: Where to output pretty printed table.
        dataframe: existing pandas dataframe object.

    Returns:
        A TableD object.

    Example:
        >>> new()
        <tabled.tabled.TableD object at 0x...>
    """

    if dataframe is not None:
        headings = list(dataframe.columns)
        data = dataframe.values.tolist()

    return TableD(headings or [], data or [], style, align, device)
