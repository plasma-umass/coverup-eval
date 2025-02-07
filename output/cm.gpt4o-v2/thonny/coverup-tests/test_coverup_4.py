# file: thonny/roughparse.py:654-656
# asked: {"lines": [654, 655, 656], "branches": []}
# gained: {"lines": [654, 655, 656], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.str = "def foo():\n    pass\n"
    parser.goodlines = [0, 1, 2]
    parser.study_level = 1
    return parser

def test_get_last_stmt_bracketing(rough_parser):
    result = rough_parser.get_last_stmt_bracketing()
    assert result is not None
    assert isinstance(result, tuple)
    assert rough_parser.study_level == 2
    assert rough_parser.stmt_bracketing == result
