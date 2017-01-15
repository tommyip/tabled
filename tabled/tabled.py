"""
tableD: Table for Humans?

Author: Tommy Ip <hkmp7tommy@gmail.com>
License: MIT
Github repository: https://github.com/tommyip/tabled
Python version: 3.5

This is the main python module for tableD. Please read our documentation for
detailed usage information and developer guide.
"""

from typing import List, Any, Text


class TableD:
    """
    This is the public interface for TableD.
    """
    def __init__(self,
                 headings: List[Text] = [],
                 data: List[List[Any]] = [],
                 style: Text = 'default') -> None:
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

        self.headings = headings
        self.data = data
        self.style = style

    def add_row(self, row: List[Any] = []) -> None:
        """
        Append a single row to instance table. If no argument is passed in, a
        blank row would be inserted.

        >>> table = TableD()
        >>> table.add_row(['x1', 'x2', 'x3'])
        """
        pass

    def add_rows(self, rows: List[List[Any]]) -> None:
        """
        Append multiple row to instance table.

        >>> table = TableD()
        >>> table.add_rows([['x1', 'x2', 'x3'],
        ...                 ['y1', 'y2', 'y3']])
        """
        pass

    def show(self) -> None:
        """
        Pretty print data in table format.
        """
        pass
