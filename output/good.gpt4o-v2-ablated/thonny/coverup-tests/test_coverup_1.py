# file: thonny/roughparse.py:163-165
# asked: {"lines": [163, 164, 165], "branches": []}
# gained: {"lines": [163, 164, 165], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    return RoughParser(indent_width=4, tabwidth=8)

def test_rough_parser_initialization(rough_parser):
    assert rough_parser.indent_width == 4
    assert rough_parser.tabwidth == 8
