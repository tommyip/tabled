"""
tabled.tabled
~~~~~~~~~~~~~

:synopsis: Pretty print data in tabular format.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

from typing import List, Any, Text, Optional


class TableD:
    """ tableD's main interface. """

    def __init__(self,
                 headings: Optional[List[Text]] = None,
                 data: Optional[List[List[Any]]] = None,
                 style: Text = 'default',
                 device: Text = 'stdout') -> None:
        """ Initialize data storage engine for TableD.

        Args:
            headings: Valid list of unicode strings for column headings.
            data: Nested list of cell data.
            style: Visual styling of the output table.
            device: Where should the output be presented.

        Example:
            >>> TableD(
            ...     ['Repo', 'Author', 'Url'],
            ...     [['tableD', 'Me', 'http://github.com/tommyip/tabled'],
            ...      ['Exmaple', 'Someone', 'http://example.com']],
            ...     'fancy'
            ... )
            <tabled.tabled.TableD object at 0x...>
        """

        # Python gotcha: mutable default argument
        self.headings = headings if headings else []
        self.data = data if data else []
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
        """ Append multiple rows to table.

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
