# file: src/blib2to3/pgen2/grammar.py:125-127
# asked: {"lines": [127], "branches": []}
# gained: {"lines": [127], "branches": []}

import pytest
import pickle
from blib2to3.pgen2.grammar import Grammar

def test_loads(monkeypatch):
    # Create a mock for the _update method
    def mock_update(self, attrs):
        for k, v in attrs.items():
            setattr(self, k, v)
    
    monkeypatch.setattr(Grammar, "_update", mock_update)
    
    # Create a sample dictionary to pickle
    sample_data = {'key1': 'value1', 'key2': 'value2'}
    pkl_data = pickle.dumps(sample_data)
    
    # Create a Grammar instance and call loads
    grammar = Grammar()
    grammar.loads(pkl_data)
    
    # Assert that the attributes were set correctly
    assert grammar.key1 == 'value1'
    assert grammar.key2 == 'value2'
