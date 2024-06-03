# file src/blib2to3/pytree.py:546-570
# lines [566, 567]
# branches ['565->566']

import pytest
from blib2to3.pytree import BasePattern

class MockNode:
    def __init__(self, type, content):
        self.type = type
        self.content = content

class TestBasePattern(BasePattern):
    def __init__(self, type=None, content=None, name=None):
        self.type = type
        self.content = content
        self.name = name

    def _submatch(self, node, results):
        # Mock implementation of _submatch to trigger the desired code path
        if node.content == self.content:
            if results is not None:
                results['mock'] = node
            return True
        return False

def test_basepattern_match():
    pattern = TestBasePattern(type='mock_type', content='mock_content', name='mock_name')
    node = MockNode(type='mock_type', content='mock_content')
    results = {}

    assert pattern.match(node, results) is True
    assert 'mock' in results
    assert results['mock'] == node
    assert 'mock_name' in results
    assert results['mock_name'] == node
