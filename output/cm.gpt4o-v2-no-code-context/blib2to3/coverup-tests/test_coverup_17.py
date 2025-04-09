# file: src/blib2to3/pytree.py:444-452
# asked: {"lines": [444, 445, 446, 447, 448, 449, 450, 451], "branches": []}
# gained: {"lines": [444, 445, 446, 447, 448, 449, 450, 451], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_clone():
    # Create a Leaf instance with all necessary attributes
    leaf = Leaf(type=1, value='value', context=('', (1, 1)), fixers_applied=['fixer1'])

    # Clone the leaf
    cloned_leaf = leaf.clone()

    # Assertions to verify the clone is correct
    assert cloned_leaf.type == leaf.type
    assert cloned_leaf.value == leaf.value
    assert cloned_leaf.prefix == leaf.prefix
    assert cloned_leaf.lineno == leaf.lineno
    assert cloned_leaf.column == leaf.column
    assert cloned_leaf.fixers_applied == leaf.fixers_applied

    # Ensure the cloned object is a different instance
    assert cloned_leaf is not leaf
