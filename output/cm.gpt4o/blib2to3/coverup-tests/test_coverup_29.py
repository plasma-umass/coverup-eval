# file src/blib2to3/pgen2/parse.py:190-203
# lines [190, 192, 194, 195, 197, 198, 199, 200, 201, 202, 203]
# branches ['192->194', '192->200', '198->199', '198->200', '201->202', '201->203']

import pytest
from blib2to3.pgen2.parse import Parser, ParseError
from blib2to3.pgen2.grammar import Grammar
from blib2to3.pgen2.token import NAME, NUMBER
from unittest.mock import Mock

@pytest.fixture
def parser():
    grammar = Grammar()
    grammar.keywords = {'if': 1, 'else': 2}
    grammar.tokens = {NAME: 3, NUMBER: 4}
    p = Parser(grammar)
    p.used_names = set()
    return p

def test_classify_name_token(parser):
    context = Mock()
    type = NAME
    value = 'variable'
    result = parser.classify(type, value, context)
    assert result == 3
    assert 'variable' in parser.used_names

def test_classify_keyword_token(parser):
    context = Mock()
    type = NAME
    value = 'if'
    result = parser.classify(type, value, context)
    assert result == 1
    assert 'if' in parser.used_names

def test_classify_unknown_token(parser):
    context = Mock()
    type = 999  # some unknown token type
    value = 'unknown'
    with pytest.raises(ParseError) as excinfo:
        parser.classify(type, value, context)
    assert str(excinfo.value) == f"bad token: type={type}, value='{value}', context={context}"

def test_classify_known_token(parser):
    context = Mock()
    type = NUMBER
    value = '123'
    result = parser.classify(type, value, context)
    assert result == 4
