# file: thonny/roughparse.py:524-550
# asked: {"lines": [524, 526, 527, 528, 529, 530, 531, 532, 534, 535, 536, 537, 538, 539, 542, 546, 547, 548, 549, 550], "branches": [[534, 535], [534, 546], [536, 537], [536, 542], [547, 548], [547, 549]]}
# gained: {"lines": [524, 526, 527, 528, 529, 530, 531, 532, 534, 535, 536, 537, 538, 539, 550], "branches": [[534, 535], [536, 537]]}

import pytest
from thonny.roughparse import RoughParser, C_BRACKET, _itemre

class MockRoughParser(RoughParser):
    def __init__(self, str, continuation, lastopenbracketpos, indent_width, tabwidth):
        self.str = str
        self.continuation = continuation
        self.lastopenbracketpos = lastopenbracketpos
        self.indent_width = indent_width
        self.tabwidth = tabwidth

    def _study2(self):
        pass

@pytest.fixture
def mock_parser():
    return MockRoughParser(
        str="def foo():\n    [1, 2, 3\n    , 4, 5, 6]\n",
        continuation=C_BRACKET,
        lastopenbracketpos=14,
        indent_width=4,
        tabwidth=8
    )

def test_compute_bracket_indent_item_found(mock_parser):
    result = mock_parser.compute_bracket_indent()
    assert result == 4  # 4 spaces from indentation

def test_compute_bracket_indent_no_item_found(mock_parser):
    mock_parser.str = "def foo():\n    [\n    ]\n"
    mock_parser.lastopenbracketpos = 12
    result = mock_parser.compute_bracket_indent()
    assert result == 4  # 4 spaces from indentation
