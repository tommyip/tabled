"""
tests.pretty_print
~~~~~~~~~~~~~~~~~~

:synopsis: Test utility functions.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

from tabled.utils import max_width, rotate_table


class TestMaxWidth:

    def test_normal(self) -> None:
        column = ['Some text', 'Some more text', 'short', 'def test():',
                  'This is a very long line of text', 'More!!']
        assert max_width(column) == 32

    def test_single_element(self) -> None:
        assert max_width(['Wow this is long']) == 16


class TestRotateTable:
    table = [['a1', 'b1', 'c1'],
             ['a2', 'b2', 'c2'],
             ['a3', 'b3', 'c3']]

    def test_normal(self) -> None:
        expected = [['a1', 'a2', 'a3'],
                    ['b1', 'b2', 'b3'],
                    ['c1', 'c2', 'c3']]

        assert rotate_table(TestRotateTable.table) == expected

    def test_reversible(self) -> None:
        rotate_twice = rotate_table(rotate_table(TestRotateTable.table))

        assert rotate_twice == TestRotateTable.table

    def test_asymmetric_list(self) -> None:
        asymmetric_table = [['a', 'b', 'c', 'd', 'e'],
                            ['1', '2', '3', '4', '5']]

        expected = [['a', '1'],
                    ['b', '2'],
                    ['c', '3'],
                    ['d', '4'],
                    ['e', '5']]

        assert rotate_table(asymmetric_table) == expected

    def test_single_column(self) -> None:
        column = [['a'], ['b'], ['c'], ['d']]
        row = [['a', 'b', 'c', 'd']]

        assert rotate_table(column) == row
