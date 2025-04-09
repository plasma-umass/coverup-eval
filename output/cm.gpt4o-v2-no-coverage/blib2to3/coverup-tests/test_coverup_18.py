# file: src/blib2to3/pytree.py:444-452
# asked: {"lines": [444, 445, 446, 447, 448, 449, 450, 451], "branches": []}
# gained: {"lines": [444, 445, 446, 447, 448, 449, 450, 451], "branches": []}

import pytest
from blib2to3.pytree import Leaf

@pytest.fixture
def leaf_instance():
    return Leaf(type=1, value="value", context=("prefix", (1, 1)), fixers_applied=[])

def test_leaf_clone(leaf_instance):
    cloned_leaf = leaf_instance.clone()
    
    assert cloned_leaf.type == leaf_instance.type
    assert cloned_leaf.value == leaf_instance.value
    assert cloned_leaf.prefix == leaf_instance.prefix
    assert cloned_leaf.lineno == leaf_instance.lineno
    assert cloned_leaf.column == leaf_instance.column
    assert cloned_leaf.fixers_applied == leaf_instance.fixers_applied
    assert cloned_leaf is not leaf_instance
