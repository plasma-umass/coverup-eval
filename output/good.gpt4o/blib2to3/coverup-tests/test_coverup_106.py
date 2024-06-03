# file src/blib2to3/pytree.py:885-900
# lines []
# branches ['893->891', '894->893']

import pytest
from blib2to3.pytree import WildcardPattern

def test_wildcard_pattern_bare_name_matches():
    # Mocking the LeafPattern and its match method
    class MockLeafPattern:
        def match(self, node, results):
            # Only match the first node to ensure the loop runs multiple times
            return node == "node1"

    # Create a WildcardPattern instance with a mock content
    wildcard_pattern = WildcardPattern(content=[[MockLeafPattern()]])
    wildcard_pattern.name = "test"

    # Create a list of mock nodes
    nodes = ["node1", "node2", "node3"]

    # Call the _bare_name_matches method
    count, results = wildcard_pattern._bare_name_matches(nodes)

    # Assertions to verify the postconditions
    assert count == 1  # Only the first node should match
    assert results == {"test": nodes[:1]}

    # Clean up if necessary (not needed in this case as no external state is modified)

