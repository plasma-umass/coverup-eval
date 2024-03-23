# file src/blib2to3/pgen2/grammar.py:125-127
# lines [125, 127]
# branches []

import pickle
import pytest
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def grammar():
    return Grammar()

def test_grammar_loads(grammar, mocker):
    # Mock the _update method to ensure it is called with correct data
    mock_update = mocker.patch.object(grammar, '_update')
    
    # Create a dummy grammar table to be pickled
    dummy_grammar_table = {'dummy_key': 'dummy_value'}
    pickled_dummy_grammar_table = pickle.dumps(dummy_grammar_table)
    
    # Call the loads method with the pickled dummy grammar table
    grammar.loads(pickled_dummy_grammar_table)
    
    # Assert that the _update method was called once with the correct data
    mock_update.assert_called_once_with(dummy_grammar_table)
