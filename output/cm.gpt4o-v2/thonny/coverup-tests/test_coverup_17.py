# file: thonny/roughparse.py:392-394
# asked: {"lines": [393, 394], "branches": []}
# gained: {"lines": [393, 394], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.continuation = "test_continuation"
    return parser

def test_get_continuation_type(rough_parser, mocker):
    mocker.patch.object(rough_parser, '_study1')
    result = rough_parser.get_continuation_type()
    rough_parser._study1.assert_called_once()
    assert result == "test_continuation"
