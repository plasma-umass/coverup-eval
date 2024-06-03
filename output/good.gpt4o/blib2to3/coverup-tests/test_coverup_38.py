# file src/blib2to3/pgen2/grammar.py:119-123
# lines [119, 121, 122, 123]
# branches []

import pytest
import pickle
from pathlib import Path
from unittest import mock
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture
def mock_grammar():
    class MockGrammar(Grammar):
        def _update(self, d):
            self.data = d
    return MockGrammar()

def test_load_method(mock_grammar, tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "temp_grammar.pickle"
    
    # Data to be pickled
    data = {"key": "value"}
    
    # Pickle the data to the temporary file
    with open(temp_file, "wb") as f:
        pickle.dump(data, f)
    
    # Load the data using the load method
    mock_grammar.load(temp_file)
    
    # Assert that the data was loaded correctly
    assert mock_grammar.data == data
