# file: src/blib2to3/pytree.py:800-809
# asked: {"lines": [800, 802, 803, 804, 805, 806, 807, 808, 809], "branches": [[802, 803], [802, 809], [803, 802], [803, 804], [804, 805], [804, 808], [806, 807], [806, 808]]}
# gained: {"lines": [800, 802, 803, 804, 805, 806, 807, 808, 809], "branches": [[802, 803], [802, 809], [803, 802], [803, 804], [804, 805], [804, 808], [806, 807]]}

import pytest
from blib2to3.pytree import WildcardPattern, BasePattern

class MockWildcardPattern(WildcardPattern):
    def __init__(self):
        super().__init__(content=[['a']])  # Provide valid content to avoid initialization error

    def generate_matches(self, nodes):
        yield (len(nodes), {'a': 1})

class TestWildcardPattern:
    @pytest.fixture
    def wildcard_pattern(self):
        return MockWildcardPattern()

    def test_match_seq_no_results(self, wildcard_pattern):
        nodes = [1, 2, 3]
        assert wildcard_pattern.match_seq(nodes) is True

    def test_match_seq_with_results(self, wildcard_pattern):
        nodes = [1, 2, 3]
        results = {}
        wildcard_pattern.name = 'test'
        assert wildcard_pattern.match_seq(nodes, results) is True
        assert results == {'a': 1, 'test': nodes}

    def test_match_seq_no_match(self, wildcard_pattern, mocker):
        nodes = [1, 2, 3]
        mocker.patch.object(wildcard_pattern, 'generate_matches', return_value=[(2, {})])
        assert wildcard_pattern.match_seq(nodes) is False
