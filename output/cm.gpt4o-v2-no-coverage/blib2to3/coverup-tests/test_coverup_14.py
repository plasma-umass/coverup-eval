# file: src/blib2to3/pgen2/pgen.py:80-88
# asked: {"lines": [80, 81, 82, 83, 84, 85, 87, 88], "branches": [[84, 85], [84, 88]]}
# gained: {"lines": [80, 81, 82, 83, 84, 85, 87, 88], "branches": [[84, 85], [84, 88]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator
from blib2to3.pgen2.grammar import Grammar as PgenGrammar
from unittest.mock import MagicMock

@pytest.fixture
def parser_generator():
    pg = ParserGenerator.__new__(ParserGenerator)
    pg.first = {}
    return pg

def test_make_first_empty(parser_generator):
    c = PgenGrammar()
    parser_generator.first = {'test': {}}
    result = parser_generator.make_first(c, 'test')
    assert result == {}

def test_make_first_non_empty(parser_generator):
    c = PgenGrammar()
    parser_generator.first = {'test': {'label1': 1, 'label2': 1}}
    parser_generator.make_label = MagicMock(side_effect=lambda c, label: hash(label))
    result = parser_generator.make_first(c, 'test')
    expected = {hash('label1'): 1, hash('label2'): 1}
    assert result == expected
    assert parser_generator.make_label.call_count == 2
