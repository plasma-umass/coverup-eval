# file: src/blib2to3/pytree.py:951-978
# asked: {"lines": [951, 966, 967, 969, 970, 971, 972, 974, 975, 976, 977, 978], "branches": [[966, 967], [966, 969], [970, 0], [970, 971], [971, 972], [971, 974], [974, 970], [974, 975]]}
# gained: {"lines": [951, 966, 967, 969, 970, 971, 972, 974, 975, 976, 977, 978], "branches": [[966, 967], [966, 969], [970, 0], [970, 971], [971, 972], [971, 974], [974, 970], [974, 975]]}

import pytest
from blib2to3.pytree import generate_matches, BasePattern

class MockPattern(BasePattern):
    def __init__(self, match_result):
        self.match_result = match_result

    def generate_matches(self, nodes):
        if self.match_result:
            yield (1, {'match': True})
        else:
            yield (0, {})

def test_generate_matches_no_patterns():
    patterns = []
    nodes = ['node1', 'node2']
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(0, {})]

def test_generate_matches_single_pattern_match():
    patterns = [MockPattern(True)]
    nodes = ['node1', 'node2']
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(1, {'match': True})]

def test_generate_matches_single_pattern_no_match():
    patterns = [MockPattern(False)]
    nodes = ['node1', 'node2']
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(0, {})]

def test_generate_matches_multiple_patterns():
    patterns = [MockPattern(True), MockPattern(True)]
    nodes = ['node1', 'node2']
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(2, {'match': True, 'match': True})]

def test_generate_matches_partial_match():
    patterns = [MockPattern(True), MockPattern(False)]
    nodes = ['node1', 'node2']
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(1, {'match': True})]

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: monkeypatch or other setup steps
    yield
    # Teardown: clean up after tests
