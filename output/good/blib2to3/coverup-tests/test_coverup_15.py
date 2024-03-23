# file src/blib2to3/pytree.py:444-452
# lines [444, 445, 446, 447, 448, 449, 450, 451]
# branches []

import pytest
from blib2to3.pytree import Leaf

@pytest.fixture
def leaf_instance():
    leaf = Leaf(1, "value", ("prefix", (1, 0)), fixers_applied=["fixer1"])
    yield leaf
    # No cleanup required for this test as we are not modifying any global state

def test_leaf_clone(leaf_instance):
    # Clone the leaf instance
    cloned_leaf = leaf_instance.clone()

    # Assertions to check if the cloned leaf has the same attributes as the original
    assert cloned_leaf.type == leaf_instance.type
    assert cloned_leaf.value == leaf_instance.value
    assert cloned_leaf.prefix == leaf_instance.prefix
    assert cloned_leaf.lineno == leaf_instance.lineno
    assert cloned_leaf.column == leaf_instance.column
    assert cloned_leaf.fixers_applied == leaf_instance.fixers_applied

    # Ensure that the cloned leaf is indeed a different object
    assert cloned_leaf is not leaf_instance
