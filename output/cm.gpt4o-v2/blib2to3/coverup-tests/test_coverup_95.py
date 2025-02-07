# file: src/blib2to3/pgen2/parse.py:190-203
# asked: {"lines": [192, 194, 195, 197, 198, 199, 200, 201, 202, 203], "branches": [[192, 194], [192, 200], [198, 199], [198, 200], [201, 202], [201, 203]]}
# gained: {"lines": [192, 194, 195, 197, 198, 199, 200, 201, 202, 203], "branches": [[192, 194], [192, 200], [198, 199], [198, 200], [201, 202], [201, 203]]}

import pytest
from blib2to3.pgen2 import token
from blib2to3.pgen2.parse import Parser, ParseError

@pytest.fixture
def parser():
    class Grammar:
        keywords = {'if': 1, 'else': 2}
        tokens = {token.NAME: 3, token.NUMBER: 4}
    
    class TestParser(Parser):
        def __init__(self):
            self.grammar = Grammar()
            self.used_names = set()
    
    return TestParser()

def test_classify_name_token(parser):
    context = ('', (0, 0))
    type = token.NAME
    value = 'if'
    result = parser.classify(type, value, context)
    assert result == 1
    assert 'if' in parser.used_names

def test_classify_name_token_not_keyword(parser):
    context = ('', (0, 0))
    type = token.NAME
    value = 'variable'
    result = parser.classify(type, value, context)
    assert result == 3
    assert 'variable' in parser.used_names

def test_classify_non_name_token(parser):
    context = ('', (0, 0))
    type = token.NUMBER
    value = '123'
    result = parser.classify(type, value, context)
    assert result == 4

def test_classify_bad_token(parser):
    context = ('', (0, 0))
    type = 999  # Invalid token type
    value = 'invalid'
    with pytest.raises(ParseError) as excinfo:
        parser.classify(type, value, context)
    assert excinfo.value.msg == 'bad token'
    assert excinfo.value.type == type
    assert excinfo.value.value == value
    assert excinfo.value.context == context
