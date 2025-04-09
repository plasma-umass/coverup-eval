# file: src/blib2to3/pytree.py:365-367
# asked: {"lines": [365, 366, 367], "branches": []}
# gained: {"lines": [365, 366, 367], "branches": []}

import pytest
from blib2to3.pytree import Node

class MockBase:
    pass

class MockNL:
    def __init__(self):
        self.parent = None

@pytest.fixture
def mock_node():
    class MockNode(Node, MockBase):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    return MockNode

def test_invalidate_sibling_maps(mock_node):
    node = mock_node(type=256, children=[MockNL(), MockNL()])
    node.invalidate_sibling_maps()
    assert node.prev_sibling_map is None
    assert node.next_sibling_map is None
