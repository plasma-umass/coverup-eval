# file: src/blib2to3/pytree.py:582-590
# asked: {"lines": [582, 588, 589, 590], "branches": [[589, 0], [589, 590]]}
# gained: {"lines": [582, 588, 589, 590], "branches": [[589, 0], [589, 590]]}

import pytest
from blib2to3.pytree import BasePattern

class MockNode:
    def __init__(self, value):
        self.value = value

@pytest.fixture
def mock_node():
    return MockNode(value="test")

@pytest.fixture
def base_pattern():
    class TestPattern(BasePattern):
        def match(self, node, results):
            results['matched'] = node.value
            return True
    return TestPattern()

def test_generate_matches_with_nodes(base_pattern, mock_node):
    nodes = [mock_node]
    matches = list(base_pattern.generate_matches(nodes))
    assert len(matches) == 1
    assert matches[0] == (1, {'matched': 'test'})

def test_generate_matches_without_nodes(base_pattern):
    nodes = []
    matches = list(base_pattern.generate_matches(nodes))
    assert len(matches) == 0
