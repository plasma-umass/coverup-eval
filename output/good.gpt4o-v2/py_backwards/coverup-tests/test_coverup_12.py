# file: py_backwards/transformers/six_moves.py:198-206
# asked: {"lines": [198, 199, 200, 201, 202, 203, 204, 205, 206], "branches": [[200, 0], [200, 201], [201, 200], [201, 202], [202, 203], [202, 205], [205, 201], [205, 206]]}
# gained: {"lines": [198, 199, 200, 201, 202, 203, 204, 205, 206], "branches": [[200, 0], [200, 201], [201, 200], [201, 202], [202, 203], [202, 205], [205, 206]]}

import pytest
from py_backwards.transformers.six_moves import _get_rewrites
from py_backwards.utils.helpers import eager
from py_backwards.transformers.six_moves import MovedAttribute, MovedModule, prefixed_moves

def test_get_rewrites_moved_attribute():
    # Setup
    test_moves = [
        ('', [MovedAttribute('name', 'old_mod', 'new_mod', 'old_attr', 'new_attr')])
    ]
    
    # Monkeypatch prefixed_moves
    original_prefixed_moves = prefixed_moves[:]
    prefixed_moves[:] = test_moves
    
    # Execute
    rewrites = _get_rewrites()
    
    # Verify
    assert rewrites == [('new_mod.new_attr', 'six.moves.name')]
    
    # Cleanup
    prefixed_moves[:] = original_prefixed_moves

def test_get_rewrites_moved_module():
    # Setup
    test_moves = [
        ('', [MovedModule('name', 'old', 'new')])
    ]
    
    # Monkeypatch prefixed_moves
    original_prefixed_moves = prefixed_moves[:]
    prefixed_moves[:] = test_moves
    
    # Execute
    rewrites = _get_rewrites()
    
    # Verify
    assert rewrites == [('new', 'six.moves.name')]
    
    # Cleanup
    prefixed_moves[:] = original_prefixed_moves
