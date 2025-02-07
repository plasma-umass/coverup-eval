# file: src/blib2to3/pgen2/pgen.py:144-175
# asked: {"lines": [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157, 158, 159, 160, 161, 163, 164, 165, 166, 167, 168, 169, 170, 172, 174, 175], "branches": [[150, 151], [150, 165], [151, 152], [151, 163], [152, 153], [152, 157], [154, 155], [154, 160], [166, 167], [166, 175], [167, 166], [167, 168], [168, 169], [168, 174]]}
# gained: {"lines": [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157, 158, 159, 160, 161, 163, 164, 165, 166, 167, 168, 169, 170, 172, 174, 175], "branches": [[150, 151], [150, 165], [151, 152], [151, 163], [152, 153], [152, 157], [154, 155], [154, 160], [166, 167], [166, 175], [167, 166], [167, 168], [168, 169], [168, 174]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator
from typing import Dict, List, Text
from unittest.mock import MagicMock

class MockDFAState:
    def __init__(self, arcs):
        self.arcs = arcs

@pytest.fixture
def parser_generator(monkeypatch):
    def mock_init(self, filename, stream=None):
        self.dfas = {
            'A': [MockDFAState({'B': 1, 'c': 2})],
            'B': [MockDFAState({'d': 3})]
        }
        self.first = {}
        self.filename = filename
        self.stream = stream
        self.generator = iter([])
        self.startsymbol = None

    monkeypatch.setattr(ParserGenerator, "__init__", mock_init)
    return ParserGenerator("dummy_filename")

def test_calcfirst_no_recursion(parser_generator):
    parser_generator.calcfirst('A')
    assert parser_generator.first['A'] == {'d': 1, 'c': 1}

def test_calcfirst_with_recursion(parser_generator):
    parser_generator.dfas['A'][0].arcs['A'] = 1
    parser_generator.first['A'] = None
    with pytest.raises(ValueError, match="recursion for rule 'A'"):
        parser_generator.calcfirst('A')

def test_calcfirst_ambiguous_rule(parser_generator):
    parser_generator.dfas['A'][0].arcs['B'] = 1
    parser_generator.dfas['B'][0].arcs['c'] = 1
    parser_generator.calcfirst('B')
    with pytest.raises(ValueError, match="rule A is ambiguous; c is in the first sets of c as well as B"):
        parser_generator.calcfirst('A')
