# file src/blib2to3/pytree.py:951-978
# lines [951, 966, 967, 969, 970, 971, 972, 974, 975, 976, 977, 978]
# branches ['966->967', '966->969', '970->exit', '970->971', '971->972', '971->974', '974->970', '974->975']

import pytest
from blib2to3.pytree import BasePattern, generate_matches

class MockPattern(BasePattern):
    def __init__(self, match_length, name=None):
        self.match_length = match_length
        self.name = name

    def generate_matches(self, nodes):
        if self.match_length <= len(nodes):
            yield self.match_length, {self.name: nodes[:self.match_length]} if self.name else {}

@pytest.fixture
def mock_pattern():
    return MockPattern

def test_generate_matches_empty_patterns(mock_pattern):
    patterns = []
    nodes = [1, 2, 3]
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(0, {})]

def test_generate_matches_single_pattern_no_rest(mock_pattern):
    patterns = [mock_pattern(1)]
    nodes = [1, 2, 3]
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(1, {})]

def test_generate_matches_single_pattern_with_rest(mock_pattern):
    patterns = [mock_pattern(1), mock_pattern(2)]
    nodes = [1, 2, 3, 4]
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(3, {})]

def test_generate_matches_multiple_patterns(mock_pattern):
    patterns = [mock_pattern(1, 'a'), mock_pattern(2, 'b')]
    nodes = [1, 2, 3, 4]
    matches = list(generate_matches(patterns, nodes))
    assert matches == [(3, {'a': [1], 'b': [2, 3]})]

def test_generate_matches_no_match(mock_pattern):
    patterns = [mock_pattern(2), mock_pattern(3)]
    nodes = [1, 2]
    matches = list(generate_matches(patterns, nodes))
    assert matches == []

def test_generate_matches_partial_match(mock_pattern):
    patterns = [mock_pattern(1), mock_pattern(3)]
    nodes = [1, 2]
    matches = list(generate_matches(patterns, nodes))
    assert matches == []

# Run the tests
if __name__ == "__main__":
    pytest.main()
