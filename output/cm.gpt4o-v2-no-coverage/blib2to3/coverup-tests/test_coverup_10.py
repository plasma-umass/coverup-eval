# file: src/blib2to3/pytree.py:800-809
# asked: {"lines": [800, 802, 803, 804, 805, 806, 807, 808, 809], "branches": [[802, 803], [802, 809], [803, 802], [803, 804], [804, 805], [804, 808], [806, 807], [806, 808]]}
# gained: {"lines": [800, 802, 803, 804, 805, 806, 807, 808, 809], "branches": [[802, 803], [802, 809], [803, 802], [803, 804], [804, 805], [804, 808], [806, 807], [806, 808]]}

import pytest
from blib2to3.pytree import WildcardPattern

class MockWildcardPattern(WildcardPattern):
    def __init__(self, *args, **kwargs):
        super().__init__(content=[['a']], *args, **kwargs)

    def generate_matches(self, nodes):
        yield (len(nodes), {'mock_key': 'mock_value'})

@pytest.fixture
def wildcard_pattern():
    return MockWildcardPattern()

def test_match_seq_full_match(wildcard_pattern):
    nodes = ['a', 'b', 'c']
    results = {}
    assert wildcard_pattern.match_seq(nodes, results) is True
    assert results == {'mock_key': 'mock_value'}

def test_match_seq_no_match(wildcard_pattern):
    nodes = ['a', 'b', 'c']
    wildcard_pattern.generate_matches = lambda x: iter([(len(x) - 1, {})])
    results = {}
    assert wildcard_pattern.match_seq(nodes, results) is False
    assert results == {}

def test_match_seq_with_name(wildcard_pattern):
    nodes = ['a', 'b', 'c']
    wildcard_pattern.name = 'test_name'
    results = {}
    assert wildcard_pattern.match_seq(nodes, results) is True
    assert results == {'mock_key': 'mock_value', 'test_name': nodes}

def test_match_seq_no_results(wildcard_pattern):
    nodes = ['a', 'b', 'c']
    assert wildcard_pattern.match_seq(nodes) is True
