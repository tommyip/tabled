"""
tableD: Table for Humans?

Author: Tommy Ip <hkmp7tommy@gmail.com>
License: MIT
Github repository: https://github.com/tommyip/tabled
Python version: 3.5
Docs: http://tabled.readthedocs.io/en/latest/

This is the main python module for tableD.
"""

from typing import List, Any, Text, Optional


class TableD:
    """ Public interface for TableD. """

    def __init__(self,
                 headings: Optional[List[Text]] = None,
                 data: Optional[List[List[Any]]] = None,
                 style: Text = 'default',
                 device: Text = 'stdout') -> None:
        """
        Initialize data storage engine for TableD. Column headings should
        be a valid lists of unicode strings while individual cells can
        contain any values. The data argument should have the same ordering
        as its headings.

        >>> TableD(
        ...     ['Repo', 'Author', 'Url'],
        ...     [['tableD', 'Tommy Ip', 'http://github.com/tommyip/tabled'],
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

        >>> table = TableD()
        >>> table.add_row(['x1', 'x2', 'x3'])
        >>> table.data
        [['x1', 'x2', 'x3']]
        """

        self.data.append(row)

    def add_rows(self, rows: List[List[Any]]) -> None:
        """ Append multiple row to table.

        >>> table = TableD()
        >>> table.add_rows([['x1', 'x2', 'x3'],
        ...                 ['y1', 'y2', 'y3']])
        >>> table.data
        [['x1', 'x2', 'x3'], ['y1', 'y2', 'y3']]
        """
        for row in rows:
            self.data.append(row)

    def show(self) -> None:
        """ Pretty print data in table format. """
        pass
