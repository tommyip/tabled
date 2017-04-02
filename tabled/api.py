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
        device: Text = 'stdout',
        dataframe: Optional[object] = None) -> TableD:
    """ Creates a new TableD object. This should be used instead of calling
    TableD's __init__() directly.

    Args:
        headings: A list of column headings which may contain any type.
        data: Nested list of lists, each cell element may contain any type.
        style: Style of pretty printed table.
        device: Output device.
        dataframe: existing pandas dataframe object.
    Returns:
        A TableD object.

    Example:
        >>> new()
        <tabled.tabled.TableD object at 0x...>
        >>> new(dataframe=new_df)
    """

<<<<<<< HEAD
    return TableD(headings or [], data or [], style, device, dataframe)
=======
    return TableD(headings or [], data or [], style, device)


def new_from_df(dataframe,
                style: Text = 'default',
                device: Text = 'stdout') -> TableD:

    """ Creates a new TableD object. This should be used instead of calling
    TableD's __init__() directly.

    Args:
        Pandas dataframe object.

    Returns:
        A TableD object.

    Example:
        >>> new()
        <tabled.tabled.TableD object at 0x...>
    """
    headings = list(dataframe.columns)
    data = dataframe.values.tolist()

    return TableD(headings, data, style, device)
>>>>>>> 86f9994ab00c49cca1249e46da59125ffa56dfd1
