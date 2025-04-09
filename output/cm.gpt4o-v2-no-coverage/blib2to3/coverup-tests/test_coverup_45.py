# file: src/blib2to3/pgen2/grammar.py:119-123
# asked: {"lines": [119, 121, 122, 123], "branches": []}
# gained: {"lines": [119, 121, 122, 123], "branches": []}

import pytest
import pickle
from pathlib import Path
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def temp_pickle_file(tmp_path):
    data = {
        'symbol2number': {'a': 1},
        'number2symbol': {1: 'a'},
        'states': [],
        'dfas': {},
        'labels': [(0, 'EMPTY')],
        'keywords': {'if': 1},
        'tokens': {1: 1},
        'symbol2label': {'a': 1},
        'start': 256,
        'async_keywords': False
    }
    file_path = tmp_path / "temp_grammar.pickle"
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)
    return file_path

def test_load(temp_pickle_file):
    grammar = Grammar()
    grammar.load(temp_pickle_file)

    assert grammar.symbol2number == {'a': 1}
    assert grammar.number2symbol == {1: 'a'}
    assert grammar.states == []
    assert grammar.dfas == {}
    assert grammar.labels == [(0, 'EMPTY')]
    assert grammar.keywords == {'if': 1}
    assert grammar.tokens == {1: 1}
    assert grammar.symbol2label == {'a': 1}
    assert grammar.start == 256
    assert grammar.async_keywords is False
