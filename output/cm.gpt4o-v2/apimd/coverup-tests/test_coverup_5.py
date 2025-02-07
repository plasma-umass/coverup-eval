# file: apimd/parser.py:294-297
# asked: {"lines": [294, 295, 297], "branches": []}
# gained: {"lines": [294, 295, 297], "branches": []}

import pytest
from apimd.parser import Parser

def test_parser_new():
    parser = Parser.new(link=True, level=2, toc=True)
    assert isinstance(parser, Parser)
    assert parser.link is True
    assert parser.b_level == 2
    assert parser.toc is True
