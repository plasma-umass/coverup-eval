# file: thonny/roughparse.py:163-165
# asked: {"lines": [163, 164, 165], "branches": []}
# gained: {"lines": [163, 164, 165], "branches": []}

import pytest
from thonny.roughparse import RoughParser

def test_roughparser_initialization():
    indent_width = 4
    tabwidth = 8
    parser = RoughParser(indent_width, tabwidth)
    
    assert parser.indent_width == indent_width
    assert parser.tabwidth == tabwidth
