"""
tabled.api
~~~~~~~~~~

:synopsis: Main interface for tabled.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

from typing import Optional, List, Any, Text

from .tabled import TableD


def new(headings: Optional[List[Any]] = None,
        data: Optional[List[List[Any]]] = None,
        style: Text = 'default',
        device: Text = 'stdout') -> TableD:
    """ This is the entry point to TableD. This should be use to initialize a
    TableD object instead of calling TableD.__init__() directly.

    Args:
        headings: A list of column headings which may contain any type.
        data: Nested list of lists, each cell element may contain any type.
        style: Style of pretty printed table.
        device: Output device.

    Returns:
        A TableD object.

    Example:
        >>> new()
        <tabled.tabled.TableD object at 0x...>
    """

    return TableD(headings or [], data or [], style, device)
