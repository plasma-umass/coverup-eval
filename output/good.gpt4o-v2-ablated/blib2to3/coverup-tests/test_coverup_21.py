# file: src/blib2to3/pgen2/grammar.py:125-127
# asked: {"lines": [125, 127], "branches": []}
# gained: {"lines": [125, 127], "branches": []}

import pytest
import pickle
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def grammar():
    return Grammar()

def test_loads_updates_grammar(grammar, mocker):
    mock_update = mocker.patch.object(grammar, '_update')
    test_data = {'key': 'value'}
    pkl = pickle.dumps(test_data)
    
    grammar.loads(pkl)
    
    mock_update.assert_called_once_with(test_data)
