"""
tabled.tabled
~~~~~~~~~~~~~

:synopsis: Pretty print data in tabular format.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

import sys
from typing import Any, List, Optional, Text

from .pretty_print import render_table
from .utils import str_list, str_nested_list, normalize_list


class TableD:
    """ Public interface for the central table abstraction.

    Attributes:
        headings: A list of column headings.
        data: Nested list of lists of cell contents.
        style: Style of pretty printer.
        align: Align cell content to either left, center or right. Default to
               setting specified in style.
        device: Where to output pretty printed table.

        _columns: The number of columns the table have.
        _output: Cached table string.
        _cache_valid: Validity of the cached table string.

    Example:
        >>> table = TableD(
        ...     ['Repository', 'Author', 'Type'],
        ...     [['tableD', 'Tommy Ip', 'Python library'],
        ...      ['VueJS', 'Evan You', 'Frontend JS framework'],
        ...      ['flask', 'Armin Ronacher', 'Web framework']]
        ... )
        >>> table.show()
        +------------+----------------+-----------------------+
        | Repository | Author         | Type                  |
        +------------+----------------+-----------------------+
        | tableD     | Tommy Ip       | Python library        |
        | VueJS      | Evan You       | Frontend JS framework |
        | flask      | Armin Ronacher | Web framework         |
        +------------+----------------+-----------------------+
    """

    def __init__(self,
                 headings: Optional[List[Any]] = None,
                 data: Optional[List[List[Any]]] = None,
                 style: Text = 'default',
                 align: Text = None,
                 device: Text = 'stdout') -> None:
        """ Initialize data storage engine for TableD. You should use
        tabled.new() to construct a TableD object. """

        self.headings = str_list(headings) if headings else []
        self.data = str_nested_list(data) if data else []
        self.style = style
        self.align = align
        self.device = device

        self._columns = len(self.headings)
        self._output = ''
        self._cache_valid = False

    def add_row(self, row: List[Any]) -> None:
        """ Append a single row to table body.

        Args:
            row: A row of data to be appended to the table.

        Example:
            >>> table = TableD()
            >>> table.add_row(['x1', 'x2', 'x3'])
            >>> table.data
            [['x1', 'x2', 'x3']]
        """

        self.data.append(str_list(row))
        self._cache_valid = False

    def add_rows(self, rows: List[List[Any]]) -> None:
        """ Append multiple rows to table body.

        Args:
            rows: Multiple rows of data to be appended to table.

        Example:
            >>> table = TableD()
            >>> table.add_rows([['x1', 'x2', 'x3'],
            ...                 ['y1', 'y2', 'y3']])
            >>> table.data
            [['x1', 'x2', 'x3'], ['y1', 'y2', 'y3']]
        """

        self.data += str_nested_list(rows)
        self._cache_valid = False

    def set_headings(self, headings: List[Any]) -> None:
        """ Set the headings of the table. Override the original headings if it
        existed.

        Args:
            headings: A list of column headings.

        Example:
            >>> table = TableD()
            >>> table.set_headings(['id', 2, 3])
            >>> table.headings
            ['id', '2', '3']
        """

        self.headings = str_list(headings)
        self._columns = len(headings)
        self._cache_valid = False

    def show(self) -> None:
        """ Generate, cache and display table to standard output. Use cached
        version if available. """

        if not self._cache_valid:
            self.data = [normalize_list(row, self._columns)
                         for row in self.data]
            self._output = render_table(self.headings, self.data,
                                        self.style, self.align)
            self._cache_valid = True

        print(self._output, file=sys.stdout)
