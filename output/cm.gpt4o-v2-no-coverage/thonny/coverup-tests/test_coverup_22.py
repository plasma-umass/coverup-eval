# file: thonny/roughparse.py:556-559
# asked: {"lines": [557, 558, 559], "branches": []}
# gained: {"lines": [557, 558, 559], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.goodlines = [0, 1, 2, 3, 4, 5]  # Mocking goodlines attribute
    return parser

def test_get_num_lines_in_stmt(rough_parser, mocker):
    mocker.patch.object(rough_parser, '_study1', return_value=None)
    result = rough_parser.get_num_lines_in_stmt()
    assert result == 1  # Since goodlines[-1] - goodlines[-2] = 5 - 4 = 1
