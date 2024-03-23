# file apimd/parser.py:269-293
# lines [269, 270, 271, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292]
# branches []

import pytest
from apimd.parser import Parser

def test_parser_initialization():
    parser = Parser(link=False, b_level=2)
    assert parser.link == False
    assert parser.b_level == 2
    assert parser.toc == False
    assert parser.level == {}
    assert parser.doc == {}
    assert parser.docstring == {}
    assert parser.imp == {}
    assert parser.root == {}
    assert parser.alias == {}
    assert parser.const == {}

@pytest.fixture
def parser():
    return Parser()

def test_parser_with_fixture(parser):
    assert parser.link == True
    assert parser.b_level == 1
    assert parser.toc == False
    assert parser.level == {}
    assert parser.doc == {}
    assert parser.docstring == {}
    assert parser.imp == {}
    assert parser.root == {}
    assert parser.alias == {}
    assert parser.const == {}
