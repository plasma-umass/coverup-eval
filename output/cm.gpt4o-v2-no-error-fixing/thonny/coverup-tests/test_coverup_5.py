# file: thonny/roughparse.py:392-394
# asked: {"lines": [392, 393, 394], "branches": []}
# gained: {"lines": [392, 393, 394], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.str = "def foo():\n    pass\n"
    parser.study_level = 0
    parser.continuation = None
    return parser

def test_get_continuation_type(rough_parser):
    rough_parser.get_continuation_type()
    assert rough_parser.continuation is not None
