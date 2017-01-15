"""
tableD: Table for Humans?

Author: Tommy Ip <hkmp7tommy@gmail.com>
License: MIT
Github repository: https://github.com/tommyip/tabled
Python version: 3.5
Docs: http://tabled.readthedocs.io/en/latest/

This is the main unittest module for tableD. We use pytest as our testing
framework, visit http://doc.pytest.org/en/latest/ for more information.

To run the test suite, execute the following in the project's root:

    $ py.test

Both unittest and doctest will be invoked.
"""

from tabled import tabled


class TestTableD:
    def test_create_new_table_blank(self) -> None:
        table = tabled.TableD()

        assert table.headings == []
        assert table.data == []
        assert table.style == 'default'
        assert table.device == 'stdout'

    def test_create_new_table(self) -> None:
        headings = ['Name', 'Age', 'Email', 'Url']
        data = [['Tommy Ip', 17, 'hkmp7tommy@gmail.com', 'example.com'],
                ['Someone', 23, 'someone@example.com', 'me.example.net']]

        table = tabled.TableD(headings, data, 'fancy', 'rst')

        assert table.headings == headings
        assert table.data == data
        assert table.style == 'fancy'
        assert table.device == 'rst'

    def test_add_row_1(self) -> None:
        data = ['x1', 'x2', 'x3']

        table = tabled.TableD()
        table.add_row(data)

        assert table.data == [data]

    def test_add_row_2(self) -> None:
        datas = [['x1', 'x2', 'x3'],
                 ['y1', 'y2', 'y3'],
                 ['z1', 'z2', 'z3']]

        table = tabled.TableD()

        for data in datas:
            table.add_row(data)

        assert table.data == datas
