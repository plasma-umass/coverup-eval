# file: thonny/roughparse.py:679-719
# asked: {"lines": [679, 682, 684, 686, 687, 689, 691, 692, 693, 694, 699, 700, 701, 702, 703, 706, 710, 711, 714, 715, 716, 719], "branches": [[691, 692], [691, 703], [701, 691], [701, 702]]}
# gained: {"lines": [679, 682, 684, 686, 687, 689, 691, 692, 693, 694, 699, 700, 701, 702, 703, 706, 710, 711, 714, 715, 716, 719], "branches": [[691, 692], [701, 702]]}

import pytest
from unittest.mock import Mock

class MockText:
    def __init__(self, indent_width, tabwidth, content):
        self.indent_width = indent_width
        self.tabwidth = tabwidth
        self.content = content

    def index(self, index):
        return index

    def get(self, start, end):
        return self.content

class MockRoughParser:
    def __init__(self, indent_width, tabwidth):
        self.indent_width = indent_width
        self.tabwidth = tabwidth
        self.str = ""
        self.lo = 0

    def set_str(self, s):
        self.str = s

    def find_good_parse_start(self, is_char_in_string):
        return 0

    def set_lo(self, lo):
        self.lo = lo

    def get_last_stmt_bracketing(self):
        return [(0, 0), (1, 1)]

@pytest.fixture
def mock_text():
    return MockText(indent_width=4, tabwidth=4, content="def foo():\n    pass\n")

@pytest.fixture
def mock_rough_parser(monkeypatch):
    monkeypatch.setattr("thonny.roughparse.RoughParser", MockRoughParser)

def test_hyperparser_init(mock_text, mock_rough_parser):
    from thonny.roughparse import HyperParser

    parser = HyperParser(mock_text, "1.0")

    assert parser.text == mock_text
    assert parser.rawtext == "def foo():\n    pass\n"
    assert parser.stopatindex == "1.end"
    assert parser.bracketing == [(0, 0), (1, 1)]
    assert parser.isopener == [False, True]
