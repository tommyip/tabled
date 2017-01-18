"""
tests.pretty_print
~~~~~~~~~~~~~~~~~~

:synopsis: Test pretty printing engine.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

import pytest

from tabled.pretty_print import left_pad, right_pad, left_right_pad, pad


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
