# file: src/blib2to3/pgen2/parse.py:190-203
# asked: {"lines": [190, 192, 194, 195, 197, 198, 199, 200, 201, 202, 203], "branches": [[192, 194], [192, 200], [198, 199], [198, 200], [201, 202], [201, 203]]}
# gained: {"lines": [190, 192, 194, 195, 197, 198, 199, 200, 201, 202, 203], "branches": [[192, 194], [192, 200], [198, 199], [198, 200], [201, 202], [201, 203]]}

import pytest
from blib2to3.pgen2.parse import Parser, ParseError
from blib2to3.pgen2.grammar import Grammar
from blib2to3.pgen2.token import NAME, NUMBER

class MockGrammar:
    def __init__(self):
        self.keywords = {}
        self.tokens = {}

@pytest.fixture
def parser():
    grammar = MockGrammar()
    parser = Parser(grammar)
    parser.used_names = set()
    return parser

def test_classify_name_token(parser):
    parser.grammar.keywords = {'def': 1}
    parser.grammar.tokens = {NAME: 2}
    assert parser.classify(NAME, 'def', None) == 1
    assert 'def' in parser.used_names

def test_classify_non_keyword_name_token(parser):
    parser.grammar.keywords = {}
    parser.grammar.tokens = {NAME: 2}
    assert parser.classify(NAME, 'variable', None) == 2
    assert 'variable' in parser.used_names

def test_classify_non_name_token(parser):
    parser.grammar.tokens = {NUMBER: 3}
    assert parser.classify(NUMBER, '123', None) == 3

def test_classify_bad_token(parser):
    parser.grammar.tokens = {}
    with pytest.raises(ParseError):
        parser.classify(NUMBER, '123', None)
