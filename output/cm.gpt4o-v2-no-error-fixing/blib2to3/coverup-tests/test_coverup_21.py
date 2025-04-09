# file: src/blib2to3/pytree.py:320-327
# asked: {"lines": [320, 321, 325, 326, 327], "branches": [[325, 326], [325, 327]]}
# gained: {"lines": [320, 321, 325, 326, 327], "branches": [[325, 326], [325, 327]]}

import pytest
from blib2to3.pytree import Node

class MockChild:
    def __init__(self, prefix):
        self.prefix = prefix
        self.parent = None

def test_node_prefix_with_children():
    child = MockChild(prefix=" ")
    node = Node(type=256, children=[child])
    assert node.prefix == " "

def test_node_prefix_without_children():
    node = Node(type=256, children=[])
    assert node.prefix == ""

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code to run before each test
    yield
    # Code to run after each test
    # Clean up any state here if necessary
