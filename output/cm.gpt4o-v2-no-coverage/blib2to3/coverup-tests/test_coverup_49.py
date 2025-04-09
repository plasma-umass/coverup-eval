# file: src/blib2to3/pytree.py:432-438
# asked: {"lines": [432, 438], "branches": []}
# gained: {"lines": [432, 438], "branches": []}

import pytest
from blib2to3.pytree import Leaf

class MockBase:
    pass

@pytest.fixture
def leaf_instance():
    class LeafWithMockBase(Leaf, MockBase):
        pass

    return LeafWithMockBase(type=1, value="value", prefix="prefix_")

def test_leaf_str(leaf_instance):
    assert str(leaf_instance) == "prefix_value"
