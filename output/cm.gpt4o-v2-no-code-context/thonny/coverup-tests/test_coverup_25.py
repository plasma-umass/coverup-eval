# file: thonny/roughparse.py:565-616
# asked: {"lines": [565, 567, 568, 569, 570, 571, 572, 573, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 598, 599, 601, 603, 606, 607, 609, 612, 613, 614, 616], "branches": [[571, 572], [571, 573], [579, 580], [579, 603], [581, 582], [581, 584], [584, 585], [584, 588], [585, 586], [585, 587], [588, 589], [588, 590], [590, 591], [590, 592], [592, 598], [592, 601], [603, 606], [603, 609], [609, 612], [609, 616], [613, 614], [613, 616]]}
# gained: {"lines": [565, 567, 568, 569, 570, 571, 572, 573, 577, 578, 579, 580, 581, 584, 588, 590, 592, 593, 594, 595, 596, 598, 599, 601, 603, 606, 607, 609, 612, 613, 614, 616], "branches": [[571, 572], [571, 573], [579, 580], [579, 603], [581, 584], [584, 588], [588, 590], [590, 592], [592, 598], [592, 601], [603, 606], [603, 609], [609, 612], [609, 616], [613, 614], [613, 616]]}

import pytest
from thonny.roughparse import RoughParser, C_BACKSLASH
import re

class MockRoughParser(RoughParser):
    def __init__(self, str, stmt_start, continuation):
        self.str = str
        self.stmt_start = stmt_start
        self.continuation = continuation
        self.tabwidth = 4

    def _study2(self):
        pass

def _match_stringre(str, i, endpos):
    # Mock function to simulate _match_stringre behavior
    class Match:
        def end(self):
            return i + 2  # Simulate matching a string of length 2

    return Match()

@pytest.fixture
def mock_parser():
    return MockRoughParser("    a = 1\n", 0, C_BACKSLASH)

def test_compute_backslash_indent_assignment(mock_parser):
    mock_parser.str = "    a = 1\n"
    mock_parser.stmt_start = 0
    mock_parser.continuation = C_BACKSLASH
    result = mock_parser.compute_backslash_indent()
    assert result == 8

def test_compute_backslash_indent_no_assignment(mock_parser):
    mock_parser.str = "    a + 1\n"
    mock_parser.stmt_start = 0
    mock_parser.continuation = C_BACKSLASH
    result = mock_parser.compute_backslash_indent()
    assert result == 6

def test_compute_backslash_indent_with_brackets(mock_parser):
    mock_parser.str = "    a = (1 + 2)\n"
    mock_parser.stmt_start = 0
    mock_parser.continuation = C_BACKSLASH
    result = mock_parser.compute_backslash_indent()
    assert result == 8

def test_compute_backslash_indent_with_string(mock_parser):
    mock_parser.str = '    a = "test"\n'
    mock_parser.stmt_start = 0
    mock_parser.continuation = C_BACKSLASH
    result = mock_parser.compute_backslash_indent()
    assert result == 8

def test_compute_backslash_indent_with_comment(mock_parser):
    mock_parser.str = "    a = 1 # comment\n"
    mock_parser.stmt_start = 0
    mock_parser.continuation = C_BACKSLASH
    result = mock_parser.compute_backslash_indent()
    assert result == 8

def test_compute_backslash_indent_with_backslash(mock_parser):
    mock_parser.str = "    a = 1 \\\n"
    mock_parser.stmt_start = 0
    mock_parser.continuation = C_BACKSLASH
    result = mock_parser.compute_backslash_indent()
    assert result == 8
