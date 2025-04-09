# file: src/blib2to3/pytree.py:885-900
# asked: {"lines": [], "branches": [[893, 891], [894, 893]]}
# gained: {"lines": [], "branches": [[894, 893]]}

import pytest
from blib2to3.pytree import WildcardPattern, BasePattern

class MockNode:
    def __init__(self, value):
        self.value = value

    def match(self, node, results):
        return self.value == node.value

def test_bare_name_matches():
    # Create a mock node list
    nodes = [MockNode(1), MockNode(2), MockNode(3)]
    
    # Create a WildcardPattern instance with content that will match the nodes
    pattern = WildcardPattern(content=[[MockNode(1)], [MockNode(2)], [MockNode(3)]], name="test")
    
    # Call the _bare_name_matches method
    count, results = pattern._bare_name_matches(nodes)
    
    # Assertions to verify the correct behavior
    assert count == 3
    assert results["test"] == nodes[:count]

    # Clean up
    del pattern
    del nodes

