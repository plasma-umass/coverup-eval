# file src/blib2to3/pytree.py:572-580
# lines [572, 578, 579, 580]
# branches ['578->579', '578->580']

import pytest
from blib2to3.pytree import BasePattern
from typing import List, Optional

class MockPattern(BasePattern):
    def match(self, node, results: Optional[dict] = None) -> bool:
        return True

@pytest.fixture
def mock_pattern():
    return MockPattern()

def test_match_seq_single_node(mock_pattern):
    node = object()  # Mock node
    result = {}
    assert mock_pattern.match_seq([node], result) is True

def test_match_seq_multiple_nodes(mock_pattern):
    nodes = [object(), object()]  # Mock nodes
    result = {}
    assert mock_pattern.match_seq(nodes, result) is False

def test_match_seq_no_nodes(mock_pattern):
    nodes = []  # No nodes
    result = {}
    assert mock_pattern.match_seq(nodes, result) is False
