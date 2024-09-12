# file: src/blib2to3/pgen2/grammar.py:119-123
# asked: {"lines": [119, 121, 122, 123], "branches": []}
# gained: {"lines": [119, 121, 122, 123], "branches": []}

import pytest
import pickle
from pathlib import Path
from unittest import mock

from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def temp_pickle_file(tmp_path):
    data = {
        'symbol2number': {'key': 1},
        'number2symbol': {1: 'key'},
        'states': [],
        'dfas': {},
        'labels': [(0, 'EMPTY')],
        'keywords': {'key': 1},
        'tokens': {1: 1},
        'symbol2label': {'key': 1},
        'start': 256,
        'async_keywords': False
    }
    file_path = tmp_path / "test.pkl"
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)
    return file_path

def test_load_method_executes_all_lines(temp_pickle_file, mocker):
    grammar = Grammar()
    mock_update = mocker.patch.object(grammar, '_update', wraps=grammar._update)
    
    grammar.load(temp_pickle_file)
    
    mock_update.assert_called_once_with({
        'symbol2number': {'key': 1},
        'number2symbol': {1: 'key'},
        'states': [],
        'dfas': {},
        'labels': [(0, 'EMPTY')],
        'keywords': {'key': 1},
        'tokens': {1: 1},
        'symbol2label': {'key': 1},
        'start': 256,
        'async_keywords': False
    })
    assert grammar.symbol2number == {'key': 1}
    assert grammar.number2symbol == {1: 'key'}
    assert grammar.keywords == {'key': 1}
    assert grammar.tokens == {1: 1}
    assert grammar.symbol2label == {'key': 1}
