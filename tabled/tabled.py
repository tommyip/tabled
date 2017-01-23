"""
tabled.tabled
~~~~~~~~~~~~~

:synopsis: Pretty print data in tabular format.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

from typing import Any, List, Optional, Text

import sys

from .pretty_print import generate_table


class TableD:
    """ tableD's main interface.

    Attributes:
        headings: Valid list of unicode strings for column headings.
        data: Nested list of cell data.
        style: Visual styling of the output table.
        device: Where should the output be presented.

    Example:
        >>> TableD(
        ...     ['Repo', 'Author', 'Url'],
        ...     [['tableD', 'Me', 'http://github.com/tommyip/tabled'],
        ...      ['Exmaple', 'Someone', 'http://example.com']]
        ... )
        <tabled.tabled.TableD object at 0x...>
    """

    def __init__(self,
                 headings: Optional[List[Text]] = None,
                 data: Optional[List[List[Any]]] = None,
                 style: Text = 'default',
                 device: Text = 'stdout') -> None:
        """ Initialize data storage engine for TableD. """

        # Python gotcha: mutable default argument
        self.headings = headings or []
        self.data = data or []
        self.style = style
        self.device = device

    def add_row(self, row: List[Any]) -> None:
        """ Append a single row to data.

        Args:
            row: A row of data to be appended to the table.

        Example:
            >>> table = TableD()
            >>> table.add_row(['x1', 'x2', 'x3'])
            >>> table.data
            [['x1', 'x2', 'x3']]
        """

        self.data.append(row)

    def add_rows(self, rows: List[List[Any]]) -> None:
        """ Append multiple rows to data.

        Args:
            rows: Multiple rows of data to be appended to table.

        Example:
            >>> table = TableD()
            >>> table.add_rows([['x1', 'x2', 'x3'],
            ...                 ['y1', 'y2', 'y3']])
            >>> table.data
            [['x1', 'x2', 'x3'], ['y1', 'y2', 'y3']]
        """

        for row in rows:
            self.data.append(row)

    def show(self) -> None:
        """ Display the generated table to standard output. """

        self._data_2_str()

        output = generate_table(self.headings, self.data, self.style)

        print(output, file=sys.stdout)

    def _data_2_str(self) -> None:
        """ Convert all fields of the table to string type. """

        self.headings = [str(heading) for heading in self.headings]
        self.data = [[str(cell) for cell in row] for row in self.data]
