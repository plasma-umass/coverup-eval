# file: src/blib2to3/pgen2/pgen.py:331-348
# asked: {"lines": [334, 335, 336, 337, 345, 346, 348], "branches": [[333, 334], [338, 345]]}
# gained: {"lines": [334, 335, 336, 337, 345, 346], "branches": [[333, 334], [338, 345]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator, NFAState, token

class MockParserGenerator(ParserGenerator):
    def __init__(self, tokens):
        self.tokens = tokens
        self.generator = iter(tokens)
        self.gettoken()

    def parse_rhs(self):
        a = NFAState()
        z = NFAState()
        return a, z

def test_parse_atom_parentheses(monkeypatch):
    tokens = [
        (token.OP, '(', None, None, None),
        (token.NAME, 'name', None, None, None),
        (token.OP, ')', None, None, None)
    ]
    parser = MockParserGenerator(tokens)

    def mock_gettoken():
        parser.type, parser.value, parser.begin, parser.end, parser.line = next(parser.generator)

    monkeypatch.setattr(parser, 'gettoken', mock_gettoken)
    monkeypatch.setattr(parser, 'expect', lambda x, y: None)

    a, z = parser.parse_atom()
    assert isinstance(a, NFAState)
    assert isinstance(z, NFAState)

def test_parse_atom_name(monkeypatch):
    tokens = [
        (token.NAME, 'name', None, None, None),
        (token.OP, '(', None, None, None)
    ]
    parser = MockParserGenerator(tokens)

    def mock_gettoken():
        parser.type, parser.value, parser.begin, parser.end, parser.line = next(parser.generator)

    monkeypatch.setattr(parser, 'gettoken', mock_gettoken)

    a, z = parser.parse_atom()
    assert isinstance(a, NFAState)
    assert isinstance(z, NFAState)
    assert len(a.arcs) == 1
    assert a.arcs[0][1] == z
    assert a.arcs[0][0] == 'name'

def test_parse_atom_string(monkeypatch):
    tokens = [
        (token.STRING, 'string', None, None, None),
        (token.OP, '(', None, None, None)
    ]
    parser = MockParserGenerator(tokens)

    def mock_gettoken():
        parser.type, parser.value, parser.begin, parser.end, parser.line = next(parser.generator)

    monkeypatch.setattr(parser, 'gettoken', mock_gettoken)

    a, z = parser.parse_atom()
    assert isinstance(a, NFAState)
    assert isinstance(z, NFAState)
    assert len(a.arcs) == 1
    assert a.arcs[0][1] == z
    assert a.arcs[0][0] == 'string'

def test_parse_atom_error(monkeypatch):
    tokens = [
        (token.NUMBER, '123', None, None, None)
    ]
    parser = MockParserGenerator(tokens)

    def mock_gettoken():
        parser.type, parser.value, parser.begin, parser.end, parser.line = next(parser.generator)

    monkeypatch.setattr(parser, 'gettoken', mock_gettoken)
    monkeypatch.setattr(parser, 'raise_error', lambda msg, *args: (_ for _ in ()).throw(SyntaxError(msg % args)))

    with pytest.raises(SyntaxError, match="expected \\(\\.\\.\\.\\) or NAME or STRING, got 2/123"):
        parser.parse_atom()
