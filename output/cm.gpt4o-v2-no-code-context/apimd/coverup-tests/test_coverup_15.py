# file: apimd/parser.py:294-297
# asked: {"lines": [294, 295, 297], "branches": []}
# gained: {"lines": [294, 295, 297], "branches": []}

import pytest
from apimd.parser import Parser

def test_parser_new():
    parser_instance = Parser.new(link=True, level=1, toc=True)
    assert isinstance(parser_instance, Parser)
    assert parser_instance.link is True
    assert parser_instance.b_level == 1
    assert parser_instance.toc is True
