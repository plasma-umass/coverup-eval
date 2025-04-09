# file: src/blib2to3/pgen2/pgen.py:144-175
# asked: {"lines": [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157, 158, 159, 160, 161, 163, 164, 165, 166, 167, 168, 169, 170, 172, 174, 175], "branches": [[150, 151], [150, 165], [151, 152], [151, 163], [152, 153], [152, 157], [154, 155], [154, 160], [166, 167], [166, 175], [167, 166], [167, 168], [168, 169], [168, 174]]}
# gained: {"lines": [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157, 158, 159, 160, 161, 163, 164, 165, 166, 167, 168, 169, 170, 172, 174, 175], "branches": [[150, 151], [150, 165], [151, 152], [151, 163], [152, 153], [152, 157], [154, 155], [154, 160], [166, 167], [166, 175], [167, 166], [167, 168], [168, 169], [168, 174]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def parser_generator():
    from blib2to3.pgen2.pgen import ParserGenerator
    pg = ParserGenerator.__new__(ParserGenerator)
    pg.dfas = {}
    pg.first = {}
    return pg

def test_calcfirst_no_recursion(parser_generator):
    state = MagicMock()
    state.arcs = {'a': 'next_state'}
    parser_generator.dfas = {'test': [state]}
    parser_generator.calcfirst('test')
    assert parser_generator.first['test'] == {'a': 1}

def test_calcfirst_with_recursion(parser_generator):
    state = MagicMock()
    state.arcs = {'test': 'next_state'}
    parser_generator.dfas = {'test': [state]}
    parser_generator.first = {'test': None}
    with pytest.raises(ValueError, match="recursion for rule 'test'"):
        parser_generator.calcfirst('test')

def test_calcfirst_with_ambiguity(parser_generator):
    state = MagicMock()
    state.arcs = {'a': 'next_state', 'b': 'next_state'}
    parser_generator.dfas = {'test': [state], 'a': [MagicMock()], 'b': [MagicMock()]}
    parser_generator.first = {'a': {'x': 1}, 'b': {'x': 1}}
    with pytest.raises(ValueError, match="rule test is ambiguous; x is in the first sets of b as well as a"):
        parser_generator.calcfirst('test')

def test_calcfirst_nested(parser_generator):
    state_a = MagicMock()
    state_a.arcs = {'b': 'next_state'}
    state_b = MagicMock()
    state_b.arcs = {'c': 'next_state'}
    parser_generator.dfas = {'a': [state_a], 'b': [state_b]}
    parser_generator.calcfirst('a')
    assert parser_generator.first['a'] == {'c': 1}
