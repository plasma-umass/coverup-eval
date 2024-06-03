# file src/blib2to3/pytree.py:220-222
# lines [221, 222]
# branches ['221->exit', '221->222']

import pytest
from unittest.mock import MagicMock

# Assuming the Base class is imported from blib2to3.pytree
from blib2to3.pytree import Base

class MockChild(Base):
    def leaves(self):
        yield "leaf"

class Derived(Base):
    def __init__(self, children=None):
        self.children = children or []

def test_base_leaves():
    # Create a mock child that will return a leaf
    mock_child = MockChild()
    mock_child.children = []

    # Create an instance of Derived with the mock child
    derived_instance = Derived(children=[mock_child])

    # Collect leaves from the derived instance
    leaves = list(derived_instance.leaves())

    # Assert that the leaves method yields the expected leaf
    assert leaves == ["leaf"]

    # Clean up
    derived_instance.children = []
