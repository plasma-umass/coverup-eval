# file: src/blib2to3/pytree.py:800-809
# asked: {"lines": [], "branches": [[806, 808]]}
# gained: {"lines": [], "branches": [[806, 808]]}

import pytest
from blib2to3.pytree import BasePattern, WildcardPattern

class TestWildcardPattern:
    @pytest.fixture
    def wildcard_pattern(self):
        class TestPattern(WildcardPattern):
            def __init__(self, name=None):
                self.name = name

            def generate_matches(self, nodes):
                yield len(nodes), {}

        return TestPattern

    def test_match_seq_with_name(self, wildcard_pattern):
        pattern = wildcard_pattern(name="test")
        nodes = [1, 2, 3]
        results = {}
        assert pattern.match_seq(nodes, results) is True
        assert results == {"test": nodes}

    def test_match_seq_without_name(self, wildcard_pattern):
        pattern = wildcard_pattern()
        nodes = [1, 2, 3]
        results = {}
        assert pattern.match_seq(nodes, results) is True
        assert results == {}

    def test_match_seq_no_results(self, wildcard_pattern):
        pattern = wildcard_pattern(name="test")
        nodes = [1, 2, 3]
        assert pattern.match_seq(nodes) is True
