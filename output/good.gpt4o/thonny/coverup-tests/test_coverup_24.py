# file thonny/roughparse.py:679-719
# lines [682, 684, 686, 687, 689, 691, 692, 693, 694, 699, 700, 701, 702, 703, 706, 710, 711, 714, 715, 716, 719]
# branches ['691->692', '691->703', '701->691', '701->702']

import pytest
from thonny.roughparse import HyperParser, RoughParser, _build_char_in_string_func

class MockText:
    def __init__(self, content, indent_width=4, tabwidth=4):
        self.content = content
        self.indent_width = indent_width
        self.tabwidth = tabwidth

    def index(self, index):
        return index

    def get(self, start, end):
        start_line = int(start.split('.')[0])
        end_line = int(end.split('.')[0])
        lines = self.content.split('\n')
        return '\n'.join(lines[start_line-1:end_line])

@pytest.fixture
def mock_text():
    content = (
        "def foo():\n"
        "    if True:\n"
        "        print('Hello, world!')\n"
        "    return 42\n"
    )
    return MockText(content)

def test_hyperparser_initialization(mock_text):
    index = "2.4"
    parser = HyperParser(mock_text, index)
    
    assert parser.text == mock_text
    assert parser.rawtext == (
        "def foo():\n"
        "    if True:"
    )
    assert parser.stopatindex == "2.end"
    assert parser.bracketing is not None
    assert parser.isopener is not None
    assert hasattr(parser, 'set_index')

    # Clean up if necessary (not much to clean up in this mock setup)
