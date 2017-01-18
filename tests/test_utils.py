"""
tests.pretty_print
~~~~~~~~~~~~~~~~~~

:synopsis: Test utility functions.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

from tabled.utils import max_width


class TestMaxWidth:

    def test_normal(self) -> None:
        column = ['Some text', 'Some more text', 'short', 'def test():',
                  'This is a very long line of text', 'More!!']
        assert max_width(column) == 32

    def test_single_element(self) -> None:
        assert max_width(['Wow this is long']) == 16
