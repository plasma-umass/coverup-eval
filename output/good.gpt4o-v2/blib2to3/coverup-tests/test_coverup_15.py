# file: src/blib2to3/pgen2/pgen.py:177-200
# asked: {"lines": [177, 178, 179, 181, 182, 183, 185, 186, 187, 188, 190, 192, 193, 194, 195, 197, 198, 199, 200], "branches": [[181, 182], [181, 199], [182, 183], [182, 185], [197, 181], [197, 198]]}
# gained: {"lines": [177, 178, 179, 181, 182, 185, 186, 187, 188, 190, 192, 193, 194, 195, 197, 198, 199, 200], "branches": [[181, 182], [181, 199], [182, 185], [197, 181], [197, 198]]}

import pytest
from blib2to3.pgen2 import token
from blib2to3.pgen2.pgen import ParserGenerator

class MockToken:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class MockGenerator:
    def __init__(self, tokens):
        self.tokens = iter(tokens)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.tokens)

class MockNFAState:
    def __init__(self):
        self.arcs = []

    def addarc(self, state):
        self.arcs.append((None, state))

class MockDFAState:
    def __init__(self, nfaset, finish):
        self.nfaset = nfaset
        self.finish = finish
        self.arcs = []

    def addarc(self, state, label):
        self.arcs.append((label, state))

    def unifystate(self, old, new):
        self.arcs = [(label, new if state == old else state) for label, state in self.arcs]

@pytest.fixture
def mock_parser_generator(monkeypatch):
    pg = ParserGenerator.__new__(ParserGenerator)
    pg.type = None
    pg.value = None
    pg.generator = None

    def mock_gettoken():
        token = next(pg.generator)
        pg.type, pg.value = token.type, token.value

    def mock_expect(type, value=None):
        if pg.type != type or (value is not None and pg.value != value):
            raise ValueError(f"Expected {type}/{value}, got {pg.type}/{pg.value}")
        val = pg.value
        mock_gettoken()
        return val

    def mock_parse_rhs():
        a = MockNFAState()
        z = MockNFAState()
        return a, z

    def mock_make_dfa(a, z):
        return [MockDFAState({a: 1}, z)]

    def mock_simplify_dfa(dfa):
        pass

    monkeypatch.setattr(pg, 'gettoken', mock_gettoken)
    monkeypatch.setattr(pg, 'expect', mock_expect)
    monkeypatch.setattr(pg, 'parse_rhs', mock_parse_rhs)
    monkeypatch.setattr(pg, 'make_dfa', mock_make_dfa)
    monkeypatch.setattr(pg, 'simplify_dfa', mock_simplify_dfa)

    return pg

def test_parse(mock_parser_generator):
    tokens = [
        MockToken(token.NAME, 'rule1'),
        MockToken(token.OP, ':'),
        MockToken(token.NEWLINE, '\n'),
        MockToken(token.NAME, 'rule2'),
        MockToken(token.OP, ':'),
        MockToken(token.NEWLINE, '\n'),
        MockToken(token.ENDMARKER, '')
    ]
    mock_parser_generator.generator = MockGenerator(tokens)
    mock_parser_generator.gettoken()

    dfas, startsymbol = mock_parser_generator.parse()

    assert 'rule1' in dfas
    assert 'rule2' in dfas
    assert startsymbol == 'rule1'
