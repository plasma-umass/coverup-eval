# file: src/blib2to3/pgen2/parse.py:190-203
# asked: {"lines": [192, 194, 195, 197, 198, 199, 200, 201, 202, 203], "branches": [[192, 194], [192, 200], [198, 199], [198, 200], [201, 202], [201, 203]]}
# gained: {"lines": [192, 194, 195, 197, 198, 199, 200, 201, 202, 203], "branches": [[192, 194], [192, 200], [198, 199], [198, 200], [201, 202], [201, 203]]}

import pytest
from blib2to3.pgen2.parse import Parser, ParseError
from blib2to3.pgen2 import token
from blib2to3.pytree import Context
from blib2to3.pgen2.grammar import Grammar

class MockGrammar(Grammar):
    def __init__(self):
        self.keywords = {'if': 1, 'else': 2}
        self.tokens = {token.NAME: 1, token.NUMBER: 2}

@pytest.fixture
def parser():
    grammar = MockGrammar()
    p = Parser(grammar)
    p.used_names = set()
    return p

def test_classify_name_token(parser):
    context = ("example.py", (1, 0))
    result = parser.classify(token.NAME, "variable", context)
    assert result == 1
    assert "variable" in parser.used_names

def test_classify_keyword_token(parser):
    context = ("example.py", (1, 0))
    result = parser.classify(token.NAME, "if", context)
    assert result == 1

def test_classify_non_name_token(parser):
    context = ("example.py", (1, 0))
    result = parser.classify(token.NUMBER, "123", context)
    assert result == 2

def test_classify_unknown_token(parser):
    context = ("example.py", (1, 0))
    with pytest.raises(ParseError) as excinfo:
        parser.classify(999, "unknown", context)
    assert excinfo.value.msg == "bad token"
    assert excinfo.value.type == 999
    assert excinfo.value.value == "unknown"
    assert excinfo.value.context == context
