# file: src/blib2to3/pgen2/grammar.py:125-127
# asked: {"lines": [125, 127], "branches": []}
# gained: {"lines": [125, 127], "branches": []}

import pytest
import pickle
from blib2to3.pgen2.grammar import Grammar

def test_loads():
    grammar = Grammar()
    data = {'key': 'value'}
    pkl = pickle.dumps(data)
    
    grammar.loads(pkl)
    
    assert grammar.key == 'value'
