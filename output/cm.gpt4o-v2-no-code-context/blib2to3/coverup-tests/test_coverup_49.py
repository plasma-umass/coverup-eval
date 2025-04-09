# file: src/blib2to3/pgen2/grammar.py:125-127
# asked: {"lines": [125, 127], "branches": []}
# gained: {"lines": [125, 127], "branches": []}

import pytest
import pickle
from blib2to3.pgen2.grammar import Grammar

class TestGrammar:
    def test_loads(self, mocker):
        # Create a mock for the _update method
        mock_update = mocker.patch.object(Grammar, '_update')

        # Create a sample data to pickle
        sample_data = {'key': 'value'}
        pkl = pickle.dumps(sample_data)

        # Create an instance of Grammar and call the loads method
        grammar = Grammar()
        grammar.loads(pkl)

        # Assert that _update was called with the correct data
        mock_update.assert_called_once_with(sample_data)
