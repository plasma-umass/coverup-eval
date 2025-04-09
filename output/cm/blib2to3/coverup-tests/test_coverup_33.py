# file src/blib2to3/pytree.py:582-590
# lines [582, 588, 589, 590]
# branches ['589->exit', '589->590']

import pytest
from blib2to3.pytree import BasePattern
from typing import List, Tuple, Iterator

class MockNode:
    def __init__(self, value):
        self.value = value

class MockPattern(BasePattern):
    def match(self, node, results):
        return node.value == 'match'

@pytest.fixture
def mock_nodes():
    return [MockNode('match'), MockNode('no match')]

def test_base_pattern_generate_matches(mock_nodes):
    pattern = MockPattern()
    matches = list(pattern.generate_matches(mock_nodes))
    assert len(matches) == 1
    assert matches[0][0] == 1
    assert isinstance(matches[0][1], dict)
