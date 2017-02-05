"""
tests.pretty_print
~~~~~~~~~~~~~~~~~~

:synopsis: Test pretty printing engine.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

import pytest

from tabled.pretty_print import (render_row, generate_table, left_pad,
                                 left_right_pad, pad, right_pad)


class TestLeftPad:

    def test_normal(self) -> None:
        assert left_pad('Python', 13) == '       Python'

    def test_same_width(self) -> None:
        assert left_pad('test.example.com', 16) == 'test.example.com'

    def test_too_narrow(self) -> None:
        with pytest.raises(ValueError):
            left_pad('Very long line of text', 5)


class TestRightPad:

    def test_normal(self) -> None:
        assert right_pad('Python', 13) == 'Python       '

    def test_same_width(self) -> None:
        assert right_pad('test.example.com', 16) == 'test.example.com'

    def test_too_narrow(self) -> None:
        with pytest.raises(ValueError):
            right_pad('Very long line of text', 5)


class TestLeftRightPad:

    def test_normal(self) -> None:
        assert left_right_pad('test', 8) == '  test  '

    def test_uneven_pad_space(self) -> None:
        assert left_right_pad('example text', 15) == ' example text  '

    def test_too_narrow(self) -> None:
        with pytest.raises(ValueError):
            left_right_pad('long string', 2)


class TestPad:

    def test_align_left(self) -> None:
        assert pad('Test string', 15, 'left') == ' Test string   '

    def test_align_right(self) -> None:
        assert pad('Another example', 19, 'right') == '   Another example '

    def test_align_center(self) -> None:
        assert pad('Some string', 15, 'center') == '  Some string  '
        assert pad('Some string', 16, 'center') == '  Some string   '

    def test_margin(self) -> None:
        assert pad('example.com', 15, margin=2) == '  example.com  '


class TestConstructRow:

    def test_normal(self) -> None:
        row = ['Python', 'PyPy', 'RPython', 'Jython', 'Cython']
        widths = [10, 11, 9, 11, 9]

        output = render_row(row, widths,
                            dict(left='|', connector='|', right='|'))
        expected = '| Python   | PyPy      | RPython | Jython    | Cython  |'

        assert output == expected

    def test_blank(self) -> None:
        row = ['', '', '', '', '']
        widths = [2, 2, 2, 2, 2]

        output = render_row(row, widths,
                            dict(left='|', connector=':', right='|'))

        assert output == '|  :  :  :  :  |'


class TestGenerateTable:

    SIMPLE_HEADING = ['x', 'f(x) = x^3']
    SIMPLE_TABLE = [[str(x), str(x ** 3)] for x in range(5)]

    def test_style_default(self) -> None:

        generated_table = generate_table(TestGenerateTable.SIMPLE_HEADING,
                                         TestGenerateTable.SIMPLE_TABLE)

        assert generated_table == ('+---+------------+\n'
                                   '| x | f(x) = x^3 |\n'
                                   '+---+------------+\n'
                                   '| 0 | 0          |\n'
                                   '| 1 | 1          |\n'
                                   '| 2 | 8          |\n'
                                   '| 3 | 27         |\n'
                                   '| 4 | 64         |\n'
                                   '+---+------------+')

    def test_style_terminal(self) -> None:
        generated_table = generate_table(TestGenerateTable.SIMPLE_HEADING,
                                         TestGenerateTable.SIMPLE_TABLE,
                                         style='terminal')

        assert generated_table == ('╔═══╦════════════╗\n'
                                   '║ x ║ f(x) = x^3 ║\n'
                                   '╠═══╬════════════╣\n'
                                   '║ 0 ║ 0          ║\n'
                                   '║ 1 ║ 1          ║\n'
                                   '║ 2 ║ 8          ║\n'
                                   '║ 3 ║ 27         ║\n'
                                   '║ 4 ║ 64         ║\n'
                                   '╚═══╩════════════╝')

    def test_textual_data(self) -> None:
        headings = ['Category', 'Type', 'Name']
        table = [['NoSQL', 'KV store', 'Aerospike'],
                 ['NoSQL', 'Document store', 'MongoDB'],
                 ['NoSQL', 'Graph', 'Neo4j'],
                 ['NoSQL', 'Tabular', 'BigTable'],
                 ['NoSQL', 'Column', 'Cassandra'],
                 ['Relational', '', 'Oracle DB'],
                 ['Relational', '', 'MySQL'],
                 ['Relational', '', 'Microsoft SQL Server']]

        expected = ('╔════════════╦════════════════╦══════════════════════╗\n'
                    '║ Category   ║ Type           ║ Name                 ║\n'
                    '╠════════════╬════════════════╬══════════════════════╣\n'
                    '║ NoSQL      ║ KV store       ║ Aerospike            ║\n'
                    '║ NoSQL      ║ Document store ║ MongoDB              ║\n'
                    '║ NoSQL      ║ Graph          ║ Neo4j                ║\n'
                    '║ NoSQL      ║ Tabular        ║ BigTable             ║\n'
                    '║ NoSQL      ║ Column         ║ Cassandra            ║\n'
                    '║ Relational ║                ║ Oracle DB            ║\n'
                    '║ Relational ║                ║ MySQL                ║\n'
                    '║ Relational ║                ║ Microsoft SQL Server ║\n'
                    '╚════════════╩════════════════╩══════════════════════╝')

        assert generate_table(headings, table, style='terminal') == expected
