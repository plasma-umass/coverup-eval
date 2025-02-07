# file: thonny/roughparse.py:524-550
# asked: {"lines": [524, 526, 527, 528, 529, 530, 531, 532, 534, 535, 536, 537, 538, 539, 542, 546, 547, 548, 549, 550], "branches": [[534, 535], [534, 546], [536, 537], [536, 542], [547, 548], [547, 549]]}
# gained: {"lines": [524, 526, 527, 528, 529, 530, 531, 532, 534, 535, 536, 537, 538, 539, 550], "branches": [[534, 535], [536, 537]]}

import pytest
from thonny.roughparse import RoughParser, _itemre, C_BRACKET

@pytest.fixture
def rough_parser():
    parser = RoughParser(indent_width=4, tabwidth=4)
    parser.str = "def foo():\n    if (a == b):\n        print(a)\n"
    parser.continuation = C_BRACKET
    parser.lastopenbracketpos = 14  # Position of '(' in the string
    return parser

def test_compute_bracket_indent_case1(rough_parser, mocker):
    mocker.patch.object(rough_parser, '_study2')
    rough_parser._study2()
    result = rough_parser.compute_bracket_indent()
    assert result == 4  # Expected indentation length

def test_compute_bracket_indent_case2(rough_parser, mocker):
    rough_parser.str = "def foo():\n    if (a == b):\n"
    rough_parser.lastopenbracketpos = 14  # Position of '(' in the string
    mocker.patch.object(rough_parser, '_study2')
    rough_parser._study2()
    result = rough_parser.compute_bracket_indent()
    assert result == 4  # Expected indentation length

def test_compute_bracket_indent_case3(rough_parser, mocker):
    rough_parser.str = "def foo():\n    if (a == b):\n    # comment\n"
    rough_parser.lastopenbracketpos = 14  # Position of '(' in the string
    mocker.patch.object(rough_parser, '_study2')
    rough_parser._study2()
    result = rough_parser.compute_bracket_indent()
    assert result == 4  # Expected indentation length

def test_compute_bracket_indent_case4(rough_parser, mocker):
    rough_parser.str = "def foo():\n    if (a == b):\n    \n"
    rough_parser.lastopenbracketpos = 14  # Position of '(' in the string
    mocker.patch.object(rough_parser, '_study2')
    rough_parser._study2()
    result = rough_parser.compute_bracket_indent()
    assert result == 4  # Expected indentation length
