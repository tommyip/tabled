"""
tests.pretty_print
~~~~~~~~~~~~~~~~~~

:synopsis: Test pretty printing engine.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

import pytest

from tabled.pretty_print import left_pad, right_pad


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
