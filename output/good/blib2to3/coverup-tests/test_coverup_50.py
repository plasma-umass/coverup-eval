# file src/blib2to3/pgen2/grammar.py:119-123
# lines [119, 121, 122, 123]
# branches []

import pytest
from pathlib import Path
from blib2to3.pgen2.grammar import Grammar
import pickle
import tempfile
import os

# Test function to improve coverage for Grammar.load
def test_grammar_load(mocker):
    # Create a temporary file to simulate the grammar pickle file
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        tmpfile_path = Path(tmpfile.name)
        # Create a mock grammar dictionary to be pickled
        mock_grammar_dict = {'key': 'value'}
        # Pickle the mock grammar dictionary into the temporary file
        pickle.dump(mock_grammar_dict, tmpfile)
    
    # Create a Grammar instance
    grammar = Grammar()
    # Mock the _update method to verify it's called with the correct argument
    mock_update = mocker.patch.object(grammar, '_update')

    # Load the grammar from the temporary pickle file
    grammar.load(tmpfile_path)

    # Verify that the _update method was called with the mock grammar dictionary
    mock_update.assert_called_once_with(mock_grammar_dict)

    # Clean up the temporary file
    os.unlink(tmpfile_path)
