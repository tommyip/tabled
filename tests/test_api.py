"""
tests.api
~~~~~~~~~

:synopsis: Test public api.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

import pandas

from tabled.api import new


class TestNew:

    def test_pandas_dataframe(self) -> None:
        headings = ['Column 1', 'Second column', '3rd column']

        df = pandas.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                              columns=headings)

        t = new(dataframe=df)

        assert t.data == [['1', '2', '3'],
                          ['4', '5', '6'],
                          ['7', '8', '9']]

        assert t.headings == headings
