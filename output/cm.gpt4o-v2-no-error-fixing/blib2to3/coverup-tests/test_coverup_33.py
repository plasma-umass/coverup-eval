# file: src/blib2to3/pgen2/grammar.py:119-123
# asked: {"lines": [119, 121, 122, 123], "branches": []}
# gained: {"lines": [119, 121, 122, 123], "branches": []}

import pytest
import pickle
from pathlib import Path
from unittest.mock import mock_open, patch

from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def mock_grammar():
    return Grammar()

def test_load_method(mock_grammar, tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "test_grammar.pickle"
    
    # Data to be pickled
    data = {'key1': 'value1', 'key2': 'value2'}
    
    # Pickle the data to the temporary file
    with open(temp_file, 'wb') as f:
        pickle.dump(data, f)
    
    # Mock the _update method to track its calls
    with patch.object(Grammar, '_update', wraps=mock_grammar._update) as mock_update:
        # Call the load method
        mock_grammar.load(temp_file)
        
        # Assert _update was called once with the correct data
        mock_update.assert_called_once_with(data)
        
        # Assert the attributes were set correctly
        assert mock_grammar.key1 == 'value1'
        assert mock_grammar.key2 == 'value2'
