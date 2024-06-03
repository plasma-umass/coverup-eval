# file src/blib2to3/pytree.py:951-978
# lines [951, 966, 967, 969, 970, 971, 972, 974, 975, 976, 977, 978]
# branches ['966->967', '966->969', '970->exit', '970->971', '971->972', '971->974', '974->970', '974->975']

import pytest
from unittest.mock import Mock
from blib2to3.pytree import generate_matches

class MockPattern:
    def __init__(self, matches):
        self.matches = matches

    def generate_matches(self, nodes):
        for match in self.matches:
            yield match

def test_generate_matches_no_patterns():
    patterns = []
    nodes = [1, 2, 3]
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(0, {})]

def test_generate_matches_single_pattern():
    patterns = [MockPattern([(1, {'a': 1})])]
    nodes = [1, 2, 3]
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(1, {'a': 1})]

def test_generate_matches_multiple_patterns():
    patterns = [
        MockPattern([(1, {'a': 1})]),
        MockPattern([(2, {'b': 2})])
    ]
    nodes = [1, 2, 3]
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(3, {'a': 1, 'b': 2})]

def test_generate_matches_nested_patterns():
    patterns = [
        MockPattern([(1, {'a': 1})]),
        MockPattern([(1, {'b': 2})]),
        MockPattern([(1, {'c': 3})])
    ]
    nodes = [1, 2, 3]
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(3, {'a': 1, 'b': 2, 'c': 3})]

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
