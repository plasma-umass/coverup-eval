# file: src/blib2to3/pytree.py:800-809
# asked: {"lines": [], "branches": [[806, 808]]}
# gained: {"lines": [], "branches": [[806, 808]]}

import pytest
from blib2to3.pytree import WildcardPattern

class MockBasePattern:
    def generate_matches(self, nodes):
        yield (len(nodes), {'mock_key': 'mock_value'})

class TestWildcardPattern(WildcardPattern, MockBasePattern):
    def __init__(self, *args, **kwargs):
        if 'content' not in kwargs:
            kwargs['content'] = [['mock_content']]
        super().__init__(*args, **kwargs)

    def generate_matches(self, nodes):
        yield (len(nodes), {'mock_key': 'mock_value'})

@pytest.fixture
def wildcard_pattern():
    return TestWildcardPattern(name='test_name')

def test_match_seq_with_name(wildcard_pattern):
    nodes = ['node1', 'node2']
    results = {}
    assert wildcard_pattern.match_seq(nodes, results) is True
    assert results == {'mock_key': 'mock_value', 'test_name': nodes}

def test_match_seq_without_name():
    pattern = TestWildcardPattern()
    nodes = ['node1', 'node2']
    results = {}
    assert pattern.match_seq(nodes, results) is True
    assert results == {'mock_key': 'mock_value'}

def test_match_seq_no_results(wildcard_pattern):
    nodes = ['node1', 'node2']
    assert wildcard_pattern.match_seq(nodes) is True
