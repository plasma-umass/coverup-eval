# file: thonny/roughparse.py:638-640
# asked: {"lines": [638, 639, 640], "branches": []}
# gained: {"lines": [638, 639, 640], "branches": []}

import pytest
from thonny.roughparse import RoughParser

class MockRoughParser(RoughParser):
    def __init__(self, indent_width, tabwidth):
        super().__init__(indent_width, tabwidth)
        self.str = ""
        self.stmt_start = 0

    def _study2(self):
        pass

def test_is_block_closer(mocker):
    parser = MockRoughParser(indent_width=4, tabwidth=4)
    parser.str = "}"
    parser.stmt_start = 0

    mock_closere = mocker.patch("thonny.roughparse._closere", return_value=True)
    
    assert parser.is_block_closer() is True
    mock_closere.assert_called_once_with(parser.str, parser.stmt_start)

    mock_closere.reset_mock(return_value=False)
    mock_closere.return_value = None
    
    assert parser.is_block_closer() is False
    mock_closere.assert_called_once_with(parser.str, parser.stmt_start)
