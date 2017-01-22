"""
tests.tabled
~~~~~~~~~~~~~

:synopsis: Test main application interface of tableD.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

from tabled.tabled import TableD


class TestTableD:
    def test_create_new_table_blank(self) -> None:
        table = TableD()

        assert table.headings == []
        assert table.data == []
        assert table.style == 'default'
        assert table.device == 'stdout'

    def test_create_new_table(self) -> None:
        headings = ['Name', 'Age', 'Email', 'Url']
        data = [['Tommy Ip', 17, 'hkmp7tommy@gmail.com', 'example.com'],
                ['Someone', 23, 'someone@example.com', 'me.example.net']]

        table = TableD(headings, data, 'fancy', 'rst')

        assert table.headings == headings
        assert table.data == data
        assert table.style == 'fancy'
        assert table.device == 'rst'

    def test_add_row_1(self) -> None:
        data = ['x1', 'x2', 'x3']

        table = TableD()
        table.add_row(data)

        assert table.data == [data]

    def test_add_row_2(self) -> None:
        datas = [['x1', 'x2', 'x3'],
                 ['y1', 'y2', 'y3'],
                 ['z1', 'z2', 'z3']]

        table = TableD()

        for data in datas:
            table.add_row(data)

        assert table.data == datas

    def test_show(self, capfd) -> None:
        headings = ['x', 'f : x -> x^x']
        data = [[str(x), str(x ** x)] for x in range(1, 6)]

        TableD(headings, data).show()

        out, err = capfd.readouterr()

        assert out == ('+---+--------------+\n'
                       '| x | f : x -> x^x |\n'
                       '+---+--------------+\n'
                       '| 1 | 1            |\n'
                       '| 2 | 4            |\n'
                       '| 3 | 27           |\n'
                       '| 4 | 256          |\n'
                       '| 5 | 3125         |\n'
                       '+---+--------------+\n')
